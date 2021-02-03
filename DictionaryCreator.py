import itertools
from collections import defaultdict, Counter
import regex
from bs4 import BeautifulSoup
import re
import os

inputDir = os.curdir


def parseAct(xmlFile):
    content = []
    with open(xmlFile, encoding='utf8') as fobj:
        contents = fobj.read()
        soup = BeautifulSoup(contents, 'lxml')
        for tag in soup.find('body').find_all('p'):
            content.append(tag.text)
    return content


# read משרד המשפטים xml
texts = []


def reSub(line):
    line = regex.sub(r'\p{Pd}', '-', line)
    # line = re.sub(r'[^\w\s־-–־]', '', line)
    line = re.sub(r'[^\"\w\s-]', '', line)
    words = line.split()
    for i in range(len(words)):
        words[i] = re.sub(r'^[\"-]', '', words[i])
        words[i] = re.sub(r'[\"-]$', '', words[i])
    return words


for currentpath, folders, files in os.walk(inputDir):
    for file in files:
        if file.endswith(".xml"):
            content = parseAct(currentpath + "/" + file)
            lines = []
            for line in content:
                words = reSub(line)
                texts.append(words)


all_words = list(itertools.chain.from_iterable(texts))

# WORDS = Counter(itertools.chain.from_iterable(texts))
print()


