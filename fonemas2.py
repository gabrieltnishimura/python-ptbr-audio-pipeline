from time import sleep
from pyquery import PyQuery
import requests
import re
import math
import numpy as np

WORDS_FILE = '_words.npy'
PHONEMES_FILE = '_phonemes.npy'
letters = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'z']
words, phonemes = [], []


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def get_html(letter: str, page: str):
    url = 'http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=%s&start=%s' % (
        letter, int(page)*20)
    return requests.get(url).text


def get_result_pages(html):
    pq = PyQuery(html)
    tag = pq('td#maintext p:last').text()
    matcher = re.match(r'\w - \w* de (\w*) resultado', tag)
    if matcher:
        results = matcher.group(1)
        return math.floor(int(results) / 20)
    else:
        return 1


def loop_letter(letter):
    response = get_html(letter, 0)
    total_pages = get_result_pages(response)
    for i in range(0, total_pages):
        response = get_html(letter, i)
        pq = PyQuery(response)
        for line in pq('#rollovertable tr').items():
            word = line('td:first').text().replace('\n', '')
            phoneme = line('td:last').text().replace('\n', '')
            if word != '' and phoneme != '' and word not in words:
                words.append(word)
                phonemes.append(phoneme)
        printProgressBar(i, total_pages, prefix='Progress:',
                         suffix='Complete (' + str(total_pages) + ')', length=50)


def process():
    for letter in letters:
        print('Letter: \'' + str(letter) + '\'')
        loop_letter(letter)
        persist(letter)
        print('Finished letter: \'' + str(letter) + '\'')


def persist(letter: str):
    npwords = np.array(words)
    npphonemes = np.array(phonemes)
    np.save(letter+WORDS_FILE, npwords)
    np.save(letter+PHONEMES_FILE, npphonemes)


process()
