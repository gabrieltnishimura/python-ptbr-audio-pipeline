import numpy as np

WORDS_FILE = 'words.npy'
PHONEMES_FILE = 'phonemes.npy'
DICT_FILE = 'dict.npy'
words, phonemes = np.load(
    "phonemes/"+WORDS_FILE), np.load("phonemes/"+PHONEMES_FILE)

concatenated_words, concatenated_phonemes = [], []
dict = {}

i = 0
for word in words:
    dict[word.replace('·', '')] = phonemes[i].split('.')
    i += 1

np.save(DICT_FILE, dict)
