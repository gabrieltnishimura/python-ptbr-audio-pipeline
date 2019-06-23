import numpy as np

WORDS_FILE = 'words.npy'
PHONEMES_FILE = 'phonemes.npy'
DICT_FILE = 'dict.npy'
words, phonemes = np.load(
    "phonemes/"+WORDS_FILE), np.load("phonemes/"+PHONEMES_FILE)

dict = {}

i = 0
WEIRD_SEPARATOR = ' ou '
for word in words:
    word = word.replace('·', '')
    if WEIRD_SEPARATOR in phonemes[i]:
        dict[word] = phonemes[i].split(WEIRD_SEPARATOR, 1)[0].split('.')
    else:
        dict[word] = phonemes[i].split('.')
    i += 1

np.save(DICT_FILE, dict)
