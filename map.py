import numpy as np

WORDS_FILE = 'words.npy'
PHONEMES_FILE = 'phonemes.npy'
CON_WORDS_FILE = 'con_words.npy'
CON_PHONEMES_FILE = 'con_phonemes.npy'
words, phonemes = np.load(
    "phonemes/"+WORDS_FILE), np.load("phonemes/"+PHONEMES_FILE)

concatenated_words, concatenated_phonemes = [], []

i = 0
for word in words:
    concatenated_words.append(word.replace('·', ''))
    concatenated_phonemes.append(phonemes[i].split('.'))
    i += 1

np.save(CON_WORDS_FILE, np.array(concatenated_phonemes))
np.save(CON_PHONEMES_FILE, np.array(concatenated_phonemes))
