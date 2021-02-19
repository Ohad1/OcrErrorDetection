import zipfile
# import win32com.client
import os
import docx2txt
from DictionaryCreator import *
from OCRScanner import *
from nltk import bigrams
import copy
import json
import hunspell

spellchecker = hunspell.HunSpell('/usr/share/hunspell/he_IL.dic',
                                 '/usr/share/hunspell/he_IL.aff')

# ----------------------- HELP FUNCTIONS ------------------------

def IsValid(word, dictionary):
    valid = lambda w: w in dictionary or re.match('^\d+$', w) or '"' in w or re.match('^[a-z\u0590-\u05fe]{1,2}\'$', w)
    return valid(word) or all(valid(w) for w in word.split('-'))
    # return word in dictionary or re.match('^\d+$', word) or '"' in word

def IsError(word, dictionary, ocr_dict):
    if IsUndefinedNumber(word) or IsLetter(word):
        return True
    
    # if word in dictionary or re.match('^[a-z\u0590-\u05fe]{1,2}\'$', word):
    if re.match('^[a-z\u0590-\u05fe]{1,2}\'$', word):
        return False
    
    if spellchecker.spell(word) and word in ocr_dict:
        return False

    if '-' not in word:
        return True
    
    return any(IsError(w, dictionary, ocr_dict) for w in word.split('-'))    
    

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


# filename = os.path.join(baseDir, "416226.DOCx")
# my_text = docx2txt.process(f"{baseDir}\\{docx_name}")

# docWords = list(itertools.chain.from_iterable(docLines))
# print(len({w for w in docWords if w in dictionary}))
# print(len({w for w in docWords if w not in dictionary}))
# print(len(docWords))


def OcrWordToString(ocrWord):
    return f'<error>{ocrWord["word"]}<error>' if ocrWord['isError'] else ocrWord["word"]


def OcrLineToString(ocrLine):
    line = [OcrWordToString(ocrWord) for ocrWord in ocrLine]
    return " ".join(line)


with open('dict.json') as json_file:
    dictionary = json.load(json_file)


def ErrorDetection(baseDir, filename):
    filePath = f'{baseDir}/{filename}'
    docx_path = f"{filePath}.DOCx"
    pdf_path = f"{filePath}.PDF"
    txt_path = f"{filePath}.txt"
    tesseractOcrDict = create_dict_from_sec_ocr(pdf_path)
    my_text = docx2txt.process(docx_path)
    lines = my_text.split('\n\n')
    docLines = []

    for line in lines:
        words = reSub(line)
        if words:
            docLines.append(words)

    ocrLines = list(map(lambda s: [{'word': word, 'isError': False} for word in s], docLines))
    for lineIndex, ocrLine in enumerate(ocrLines):
        for wordIndex, ocrWord in enumerate(ocrLine):
            word = ocrLines[lineIndex][wordIndex]['word']
            # if not IsValid(word, dictionary) or IsUndefinedNumber(word) or IsLetter(word) or (word not in tesseractOcrDict):
            ocrLines[lineIndex][wordIndex]['isError'] = IsError(word, dictionary, tesseractOcrDict)
        bg = list(bigrams(ocrLine))
        for wordIndex, (w1, w2) in enumerate(bg):
            if IsYear(w1['word']) and IsAppendix(w2['word']):
                ocrLines[lineIndex][wordIndex + 1]['isError'] = True
        print(ocrLines[lineIndex])

    outputLines = [OcrLineToString(ocrLine) for ocrLine in ocrLines]
    with open(txt_path, 'w', encoding='utf-8') as outFile:
        for line in outputLines:
            outFile.write(f'{line}\n')


ErrorDetection(base_dir_shani, '123')
