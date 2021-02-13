import itertools
from collections import defaultdict, Counter
import regex
from bs4 import BeautifulSoup
import re
import os


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
    if 'CD' in line:
        print()
    if 'MCM' in line:
        print()
    # line = re.sub(r'[^\w\s־-–־]', '', line)
    # line = re.sub(r'[^\".\w\s-]', '', line)
    words = line.split()
    output = []
    for i in range(len(words)):
        # (re.match(r'\(\w+\)', )
        if not IsClause(words[i]):
            words[i] = re.sub(r'[^\".\w\s-]', '', words[i])
            words[i] = re.sub(r'^[\"-.]', '', words[i])
            words[i] = re.sub(r'[\"-.]$', '', words[i])
            output.append(words[i])
    output = list(filter(lambda a: a != '', output))
    return output


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
    all_words = set(itertools.chain.from_iterable(texts))
    all_words.discard('')
    return all_words


# WORDS = Counter(itertools.chain.from_iterable(texts))
# for w in all_words:
#     print(w)
# print(all_words)
