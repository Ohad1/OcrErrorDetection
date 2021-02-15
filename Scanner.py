import zipfile
# import win32com.client
import os
import docx2txt
from DictionaryCreator import *
from OCRScanner import *
from nltk import bigrams
import copy
import json

# ----------------------- HELP FUNCTIONS ------------------------

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

def IsLetter(docWord):
    return re.match('^[a-z\u0590-\u05fe]$', docWord)

def create_dict_from_sec_ocr(pdf_path):
    path_for_images = convert_pdf_to_image(pdf_path)
    change_extent_to_jpg(path_for_images)
    ocr_dict = ocr_on_images(path_for_images)
    return ocr_dict

# ----------------------- END HELP FUNCTIONS ------------------------

baseDir = 'C:\\Users\\Ohad\\PycharmProjects\\OcrErrorDetection\\PDF_DOC\\'  # Starting directory for directory walk
base_dir_shani = '/home/shanisam/OcrErrorDetection/pdf_for_ocr'

docx_name = "146884.DOCx"
pdf_name = "146884.PDF"
# pdf_path = f"{baseDir}\\{pdf_name}"
pdf_path = f"{base_dir_shani}/{pdf_name}"
ocr_dict = create_dict_from_sec_ocr(pdf_path)
# filename = os.path.join(baseDir, "416226.DOCx")
# my_text = docx2txt.process(f"{baseDir}\\{docx_name}")
my_text = docx2txt.process(f"{base_dir_shani}/{docx_name}")
lines = my_text.split('\n\n')
# print(my_text)
docLines = []
# dictionary = CreateDictionary('akn')
with open('dict.json') as json_file:
    dictionary = json.load(json_file)

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
