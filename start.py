import urllib.request
import urllib.parse
import os
from pydub import AudioSegment

import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

corpus_path = 'corpus.txt'
FOLDER = './assets/'
LABEL_FOLDER = './labels/'
LABEL_EXTENSION = 'png'
EXPORT_TO_TYPE = 'wav'
FILE_EXTENSION = '.mp3'

# Download and open audio in-memory
def processAudio(word):
    host = 'https://www.ispeech.org/p/generic/getaudio?action=convert&pitch=100&voice=brportuguesefemale&speed=0&'
    query = urllib.parse.urlencode({'text': word})
    urllib.request.urlretrieve(host + query, FOLDER + word + FILE_EXTENSION)
    song = AudioSegment.from_mp3(FOLDER + word + FILE_EXTENSION)
    return song

# Crop audio and return
def cropAudio(song):
    secondsToRemove = 2.3
    endTime = (song.duration_seconds - secondsToRemove)*1000
    extract = song[0:endTime]
    return extract

def generateSpectogram(word):
    sample_rate, samples = wavfile.read(FOLDER + word + '.' + EXPORT_TO_TYPE)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nperseg=254, nfft=254, noverlap=127)
    plt.pcolormesh(times, frequencies, spectrogram)
    plt.axis('off')
    plt.savefig(LABEL_FOLDER + word + '.' + LABEL_EXTENSION, bbox_inches='tight', pad_inches = 0)

# Open Corpus
with open(corpus_path) as fp:  
    line = fp.readline()
    while line:
        print('processing ' + line)
        word = line.strip()
        song = processAudio(word)
        extract = cropAudio(song)
        extract.export(FOLDER + word + '.' + EXPORT_TO_TYPE, format=EXPORT_TO_TYPE)
        os.remove(FOLDER + word + FILE_EXTENSION)
        generateSpectogram(word)
        line = fp.readline()



