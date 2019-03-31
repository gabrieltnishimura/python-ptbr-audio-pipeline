import urllib.request
import urllib.parse
from pydub import AudioSegment

corpus_path = 'corpus.txt'
MP3_EXTENSION = '.mp3'

# Download and open audio in-memory
def processAudio(word):
    host = 'https://www.ispeech.org/p/generic/getaudio?action=convert&pitch=100&voice=brportuguesefemale&speed=0&'
    query = urllib.parse.urlencode({'text': word})
    urllib.request.urlretrieve(host + query, word + MP3_EXTENSION)
    song = AudioSegment.from_mp3(word + MP3_EXTENSION)
    return song

# Crop audio and return
def cropAudio(song):
    secondsToRemove = 2.3
    endTime = (song.duration_seconds - secondsToRemove)*1000
    extract = song[0:endTime]
    return extract

# Open Corpus
with open(corpus_path) as fp:  
    line = fp.readline()
    while line:
        word = line.strip()
        song = processAudio(word)
        extract = cropAudio(song)
        extract.export(word + MP3_EXTENSION, format='mp3')
        line = fp.readline()
