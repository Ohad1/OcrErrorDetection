import itertools
from collections import defaultdict, Counter
import regex
from bs4 import BeautifulSoup
import re
import os
from collections import defaultdict


def parseAct(xmlFile):
    content = []
    with open(xmlFile, encoding='utf8') as fobj:
        contents = fobj.read()
        soup = BeautifulSoup(contents, 'lxml')
        for tag in soup.find('body').find_all('p'):
            content.append(tag.text)
    return content


# read משרד המשפטים xml


def IsClause(word):
    return re.match(r'\((XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\)$', word.upper()) or \
           re.match(r'\(\w\)$', word) or \
           re.match(r'\(\D\d+\)$', word) or \
           re.match(r'\(\d+\D\)$', word)


def reSub(line):
    line = regex.sub(r'\p{Pd}', '-', line)
    # line = re.sub(r'[^\w\s־-–־]', '', line)
    # line = re.sub(r'[^\".\w\s-]', '', line)
    words = line.split()
    # output = []
    for i in range(len(words)):
        # clause
        words[i] = re.sub(r'^\((XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\)', '', words[i])
        words[i] = re.sub(r'^\((xc|xl|l?x{0,3})(ix|iv|v?i{0,3})\)', '', words[i])
        words[i] = re.sub(r'\(\w\)', '', words[i])
        words[i] = re.sub(r'\(\D\d+\)', '', words[i])
        words[i] = re.sub(r'\([1-9]\d*\D\)', '', words[i])
        words[i] = re.sub(r'^[1-9]\.$', '', words[i])
        # rest
        words[i] = re.sub(r'[^\"\.\'\w\s-]', '', words[i])
        words[i] = re.sub(r'^[\"-\.]', '', words[i])
        words[i] = re.sub(r'\.$', '', words[i])
        words[i] = re.sub(r'[-\"]$', '', words[i])

        if words[i].count("'") > 1:
            words[i].strip("'")
            # output.append(words[i])
    words = list(filter(lambda a: a != '', words))
    return words


def CreateDictionary(inputDir):
    texts = []
    for currentPath, folders, files in os.walk(inputDir):
        # if len(texts) >= 10:
        #     break
        for file in files:
            if file.endswith(".xml"):
                content = parseAct(currentPath + "/" + file)
                for line in content:
                    words = reSub(line)
                    texts.append(words)
    # all_words = set(itertools.chain.from_iterable(texts))
    # all_words.discard('')
    WORDS = Counter(itertools.chain.from_iterable(texts))
    return defaultdict(int, WORDS)



# WORDS = Counter(itertools.chain.from_iterable(texts))
# for w in all_words:
#     print(w)
# print(all_words)
# words = CreateDictionary(os.curdir)
# print()