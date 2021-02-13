import zipfile
import win32com.client
import os
import docx2txt
from DictionaryCreator import *
from nltk import bigrams
import copy
import json

baseDir = 'C:\\Users\\Ohad\\PycharmProjects\\OcrErrorDetection\\PDF_DOC\\'  # Starting directory for directory walk


def IsValid(word, dictionary):
    valid = lambda w: w in dictionary or re.match('^\d+$', w) or '"' in w or re.match('^[a-z\u0590-\u05fe]{1,2}\'$', w)
    return valid(word) or all(valid(w) for w in word.split('-'))
    # return word in dictionary or re.match('^\d+$', word) or '"' in word


def IsUndefinedNumber(num):
    match = re.match('^[1-9]\d{4,5}$', num)
    return match is not None


def IsYear(year):
    match = re.match('[1-3][0-9]{3}$', year)
    return match is not None


def IsAppendix(appendix):
    match = re.match('^[1-9]\d{0,1}$', appendix)
    return match is not None


# filename = os.path.join(baseDir, "416226.DOCx")
my_text = docx2txt.process(f"{baseDir}\\147859.DOCx")
lines = my_text.split('\n\n')
# print(my_text)
docLines = []
dictionary = CreateDictionary('akn')
# with open('dict.json') as json_file:
#     dictionary = json.load(json_file)
# dictionary.add('1936')
for line in lines:
    # print(line)
    words = reSub(line)
    if words:
        docLines.append(words)
docWords = list(itertools.chain.from_iterable(docLines))
print(len({w for w in docWords if w in dictionary}))
print(len({w for w in docWords if w not in dictionary}))
print(len(docWords))

outputLines = copy.deepcopy(docLines)


def IsLetter(docWord):
    return re.match('^[a-z\u0590-\u05fe]$', docWord)


for lineIndex, docLine in enumerate(docLines):
    for wordIndex, docWord in enumerate(docLine):
        if not IsValid(docWord, dictionary) or IsUndefinedNumber(docWord) or IsLetter(docWord):
            outputLines[lineIndex][wordIndex] = f'<ש>{docWord}<ש>'
    bg = list(bigrams(docLine))
    for wordIndex, (w1, w2) in enumerate(bg):
        if IsYear(w1) and IsAppendix(w2):
            outputLines[lineIndex][wordIndex + 1] = f'<ש>{w2}<ש>'
    print(outputLines[lineIndex])

# for line in outputLines:
#     x = " ".join(line.reverse())
outputLines = [" ".join(line) for line in outputLines]
with open('147859_Output.txt', 'w', encoding='utf-8') as outFile:
    for line in outputLines:
        outFile.write(f'{line}\n')
# print(f'{w1} {w2}')

# for w in docWords:
#     print(w)
