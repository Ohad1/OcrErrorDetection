import zipfile
# import win32com.client
import os
import sys
import docx2txt
from DictionaryCreator import *
from TesseractOcrScanner import *
from nltk import bigrams
import copy
import json
import hunspell

spellchecker = hunspell.HunSpell('/usr/share/hunspell/he_IL.dic',
                                 '/usr/share/hunspell/he_IL.aff')
THRESHOLD = 10
ERROR = 'ש'

# ----------------------- HELP FUNCTIONS ------------------------

def IsDate(date):
    """
        the function checks if the given input is date.
    """
    match = re.match(r"\d{1,2}[-\.]\d{1,2}[-\.]\d{2,4}$", date)
    return match is not None


def IsUndefinedNumber(num):
    """
        the function checks if the given input is number of 5 or 6 digits.
        this number might be foot error. 
    """
    match = re.match(r'^[1-9]\d{4,5}$', num)
    return match is not None


def IsYear(year):
    """
        the function checks if the given input is year.
    """
    match = re.match(r'.*([1-3][0-9]{3})', year)
    return match is not None


def IsFootnote(footnote):
    """
        the function checks if the given input is date.
    """
    match = re.match(r'^[1-9]\d{0,1}$', footnote)
    return match is not None


def IsLetter(docWord):
    """
        the function checks if the given input is letter.
    """
    return re.match(r'^[a-z\u0590-\u05fe]$', docWord)


def IsError(word, dictionary, ocrDict):
    """
        the function checks if the given input (word) is a correct word or not 
        according to xml dictionary and ocrDict.
    """
    if IsUndefinedNumber(word) or IsLetter(word):
        return True

    if dictionary[word] >= THRESHOLD or re.match('^[a-z\u0590-\u05fe]{1,2}\'$', word) or IsDate(word) or re.match('^\d+$', word) or re.match(r'^\w+\"\w$', word):
        return False

    if spellchecker.spell(word) and word in ocrDict:
        return False

    if '-' not in word:
        return True

    return any(IsError(w, dictionary, ocrDict) for w in word.split('-'))


def create_dict_from_sec_ocr(pdf_path):
    """
        arguments:
            pdf_path - full path to pdf file
        the function returns list of words that detected from ocr scan on pdf file.
    """
    path_for_images = ConvertPdfToImage(pdf_path)
    ChangeExtentToJpg(path_for_images)
    ocr_dict = OcrOnImages(path_for_images)
    return ocr_dict

def OcrWordToString(ocrWord):
    return f'<{ERROR}>{ocrWord["word"]}<{ERROR}>' if ocrWord['isError'] else ocrWord["word"]

def OcrLineToString(ocrLine):
    line = [OcrWordToString(ocrWord) for ocrWord in ocrLine]
    return " ".join(line)

def ErrorDetection(baseDir, filename, dictionary):
    """
        arguments:
            baseDir - full path to directory of pdf and docx files.
            fileName - name of the file contains a law.
            dictionary - words from xml files

        the function creates txt file of the contect of the given law and marks errors.
    """
    filePath = os.path.join(baseDir, filename)
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
            ocrLines[lineIndex][wordIndex]['isError'] = IsError(word, dictionary, tesseractOcrDict)
        bg = list(bigrams(ocrLine))
        for wordIndex, (w1, w2) in enumerate(bg):
            if IsYear(w1['word']) and IsFootnote(w2['word']):
                ocrLines[lineIndex][wordIndex + 1]['isError'] = True

    outputLines = [OcrLineToString(ocrLine) for ocrLine in ocrLines]
    with open(txt_path, 'w', encoding='utf-8') as outFile:
        for line in outputLines:
            outFile.write(f'{line}\n')

# ----------------------- END HELP FUNCTIONS ------------------------


def main():
    with open('words.json') as json_file:
        dictionary = defaultdict(int, json.load(json_file))

    base_dir = sys.argv[1]

    pdf_files = [pdf_file for pdf_file in os.listdir(base_dir) if '.pdf' in pdf_file.lower()] 
    for pdf_file in pdf_files:
        file_name = os.path.splitext(pdf_file)[0]
        ErrorDetection(base_dir, file_name, dictionary)

if __name__ == "__main__":
    main()