import itertools
from collections import defaultdict, Counter
import regex
from bs4 import BeautifulSoup
import re
import os
from collections import defaultdict


def parseAct(xmlFile):
"""
    arguments:
        xmlFile - full legislation file in xml format
    the function returns the content inside <p> tags in the xml file.
"""
    content = []
    with open(xmlFile, encoding='utf8') as fobj:
        contents = fobj.read()
        soup = BeautifulSoup(contents, 'lxml')
        for tag in soup.find('body').find_all('p'):
            content.append(tag.text)
    return content


def IsClause(word):
"""
    the function use regular expressions and return true if "word" is clause,
    otherwise - false.
"""
    return re.match(r'\((XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\)$', word.upper()) or \
           re.match(r'\(\w\)$', word) or \
           re.match(r'\(\D\d+\)$', word) or \
           re.match(r'\(\d+\D\)$', word)


def reSub(line):
"""
    arguments:
        line - input sentence.
    Using regular experssion in order to return only the relevant words for detection 
    from 'line'.
"""
    line = regex.sub(r'\p{Pd}', '-', line)
    words = line.split()
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
    words = list(filter(lambda a: a != '', words))
    return words


def CreateDictionary(inputDir):
"""
    arguments:
        inputDir - path of directory with all the xml files.
    the function creates dictionary composed of words from the xml files and returns it.
"""
    texts = []
    for currentPath, folders, files in os.walk(inputDir):
        for file in files:
            if file.endswith(".xml"):
                content = parseAct(currentPath + "/" + file)
                for line in content:
                    words = reSub(line)
                    texts.append(words)
    WORDS = Counter(itertools.chain.from_iterable(texts))
    return defaultdict(int, WORDS)



