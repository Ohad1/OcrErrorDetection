from pdf2image import convert_from_path
import pytesseract
from PIL import Image
from DictionaryCreator import *
import os, sys


def convert_pdf_to_image(pdf_path):
"""
    arguments - 
        pdf_path: full path to pdf file.
    the function converts pdf file to directory with the name of the file, that contains 
    all the images.
"""
    curr_dir_path = os.path.dirname(pdf_path)

    # extract file + extension of file
    base = os.path.basename(pdf_path)

    # extract only file name - will be the name of folder
    file_name = os.path.splitext(base)[0]
    dir_name = f"{file_name}_img"
    path_for_images = os.path.join(curr_dir_path, dir_name)

    if not os.path.exists(path_for_images):
        # Create the directory
        os.mkdir(path_for_images)
    convert_from_path(pdf_path, output_folder=path_for_images)
    # convert_from_path(pdf_path, output_folder=path_for_images, poppler_path=r'C:\Program Files\poppler-21.02.0\Library\bin')
    return path_for_images


def change_extent_to_jpg(images_path):
"""
    arguments - 
        images_path: full path to images.
    the function converts extension of images from '.ppm' to '.jpg'
"""
    for filename in os.listdir(images_path):
        infilename = os.path.join(images_path, filename)
        if not os.path.isfile(infilename):
            continue
        oldbase = os.path.splitext(filename)
        newname = infilename.replace('.ppm', '.jpg')
        output = os.rename(infilename, newname)


def ocr_on_images(images_path):
"""
    arguments - 
        images_path: full path to images.
    the function uses the ocr library 'pytesseract' for detecting strings in the images
    and returns list of the words that found.
"""
    ocr_texts = []
    for filename in os.listdir(images_path):
        infilename = os.path.join(images_path, filename)
        if not os.path.isfile(infilename):
            continue

        # using Pillow's Image class to open the image and pytesseract to detect the string in the image
        text_from_pic = pytesseract.image_to_string(Image.open(infilename), lang='heb')
        words = reSub(text_from_pic)
        ocr_texts.append(words)
    all_words = set(itertools.chain.from_iterable(ocr_texts))
    all_words.discard('')
    return all_words