import numpy as np

WORDS_FILE = '-words.npy'
PHONEMES_FILE = '-phonemes.npy'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words, phonemes = np.array([]), np.array([])

for letter in letters:
    current_words = np.load("phonemes/"+letter+WORDS_FILE)
    current_phonemes = np.load("phonemes/"+letter+PHONEMES_FILE)
    words = np.concatenate((current_words, words))
    phonemes = np.concatenate((current_phonemes, phonemes))

np.save("phonemes/words.npy", words)
np.save("phonemes/phonemes.npy", phonemes)
