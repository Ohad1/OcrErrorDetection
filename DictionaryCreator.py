import itertools
from collections import defaultdict, Counter

from bs4 import BeautifulSoup
import re
import os

'''

'''

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
    line = re.sub(r'[^\w\s-]', '', line)
    return line


for currentpath, folders, files in os.walk(inputDir):
    for file in files:
        if file.endswith(".xml"):
            content = parseAct(currentpath + "/" + file)
            lines = []
            for line in content:
                line = reSub(line)
                texts.append(line.split())


all_words = list(itertools.chain.from_iterable(texts))
print(len(all_words))

WORDS = Counter(itertools.chain.from_iterable(texts))
print(len(WORDS))


def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N

