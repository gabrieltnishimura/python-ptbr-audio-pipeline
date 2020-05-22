import operator
import urllib.request
import urllib.parse
import os
import numpy as np
import matplotlib.pyplot as plt

from pydub import AudioSegment
from scipy import signal
from scipy.io import wavfile

POSSIBLE_PHONEMES_PATH = 'possible_phonemes.npy'
characters_list = []

dict = np.load(POSSIBLE_PHONEMES_PATH)

for phoneme in dict:
    for character in list(phoneme):
        if character not in characters_list:
            characters_list.append(character)

print(characters_list)
print(len(characters_list))
