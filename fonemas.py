from pyquery import PyQuery
import requests
import re
import math
import numpy as np

WORDS_FILE = '_words.npy'
PHONEMES_FILE = '_phonemes.npy'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words, phonemes = [], []


def get_html(letter: str, page: str):
    url = 'http://www.portaldalinguaportuguesa.org/index.php?action=fonetica&region=spx&act=list&letter=%s&start=%s' % (
        letter, int(page)*20)
    print('Letter: \'' + str(letter) + '\', page ' + str(page))
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
    print('Total pages for letter: \'' + str(letter) + ', ' + str(total_pages))
    for i in range(0, total_pages):
        response = get_html(letter, i)
        pq = PyQuery(response)
        for line in pq('#rollovertable tr').items():
            word = line('td:first').text().replace('\n', '')
            phoneme = line('td:last').text().replace('\n', '')
            if word != '' and phoneme != '' and word not in words:
                words.append(word)
                phonemes.append(phoneme)


def process():
    for letter in letters:
        loop_letter(letter)
        persist(letter)
        break


def persist(letter: str):
    npwords = np.array(words)
    npphonemes = np.array(phonemes)
    np.save(letter+WORDS_FILE, npwords)
    np.save(letter+PHONEMES_FILE, npphonemes)


process()
