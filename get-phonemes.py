import operator
import urllib.request
import urllib.parse
import os
import numpy as np
import matplotlib.pyplot as plt

from pydub import AudioSegment
from scipy import signal
from scipy.io import wavfile

DICT_PATH = 'dict.npy'
POSSIBLE_PHONEMES_PATH = 'possible_phonemes.npy'
total_phonemes = 0
phonemes_dict = {}
possible_phonemes = []
non_repeated_words_dict = {}
possible_words = []

dict = np.load(DICT_PATH, allow_pickle=True).item()

for word, phonemes in dict.items():
    total_phonemes += len(phonemes)
    for phoneme in phonemes:
        if phoneme in phonemes_dict:
            phonemes_dict[phoneme] += 1
        else:
            phonemes_dict[phoneme] = 1


exclude_phoneme_dict = {}

for word, phonemes in dict.items():
    for phoneme in phonemes:
        if phonemes_dict[phoneme] > 100 and phoneme not in exclude_phoneme_dict:
            exclude_phoneme_dict[phoneme] = phonemes_dict[phoneme]
            non_repeated_words_dict[word] = 1


plt.plot(*zip(*sorted(exclude_phoneme_dict.items(), key=operator.itemgetter(1))))
plt.show()

print(total_phonemes)
print(len(phonemes_dict))

for phoneme, _ in phonemes_dict.items():
    possible_phonemes.append(phoneme)

for word, _ in non_repeated_words_dict.items():
    possible_words.append(word)

print(possible_words)
print(len(possible_words))
