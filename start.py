import urllib.request
import urllib.parse
import os
import numpy as np
import matplotlib.pyplot as plt

from pydub import AudioSegment
from scipy import signal
from scipy.io import wavfile

corpus_path = 'corpus.txt'
DICT_PATH = 'dict.npy'
FOLDER = './assets/'
LABEL_FOLDER = './labels/'
LABEL_EXTENSION = 'png'
EXPORT_TO_TYPE = 'wav'
FILE_EXTENSION = '.mp3'


def processAudio(word):
    host = 'https://www.ispeech.org/p/generic/getaudio?action=convert&pitch=100&voice=brportuguesefemale&speed=0&'
    query = urllib.parse.urlencode({'text': word})
    urllib.request.urlretrieve(host + query, FOLDER + word + FILE_EXTENSION)
    song = AudioSegment.from_mp3(FOLDER + word + FILE_EXTENSION)
    return song


def cropAudio(song):
    secondsToRemove = 2.3
    endTime = (song.duration_seconds - secondsToRemove)*1000
    extract = song[0:endTime]
    return extract


def generateSpectogram(word):
    sample_rate, samples = wavfile.read(FOLDER + word + '.' + EXPORT_TO_TYPE)
    frequencies, times, spectrogram = signal.spectrogram(
        samples, sample_rate, nperseg=254, nfft=254, noverlap=127)
    plt.pcolormesh(times, frequencies, spectrogram)
    plt.axis('off')
    plt.savefig(LABEL_FOLDER + word + '.' + LABEL_EXTENSION,
                bbox_inches='tight', pad_inches=0)


def process(word):
    song = processAudio(word)
    extract = cropAudio(song)
    extract.export(FOLDER + word + '.' + EXPORT_TO_TYPE,
                   format=EXPORT_TO_TYPE)
    os.remove(FOLDER + word + FILE_EXTENSION)
    generateSpectogram(word)


i = 0
dict = np.load(DICT_PATH, allow_pickle=True).item()

for word, phonemes in dict.items():
    if not os.path.exists('labels/'+word+'.png'):
        print('processing ('+str(i)+') ' + word)
        process(word)
    i += 1
