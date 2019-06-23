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

dict = np.load(DICT_PATH, allow_pickle=True).item()

for word, phonemes in dict.items():
    total_phonemes += len(phonemes)
    for phoneme in phonemes:
        phonemes_dict[phoneme] = 1

print(total_phonemes)
print(len(phonemes_dict))

for phoneme, _ in phonemes_dict.items():
    possible_phonemes.append(phoneme)

np.save(POSSIBLE_PHONEMES_PATH, np.array(possible_phonemes))
