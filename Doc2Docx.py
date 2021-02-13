import os
import win32com.client
from docx2txt import docx2txt

baseDir = 'C:\\Users\\Ohad\\PycharmProjects\\OcrErrorDetection\\PDF_DOC'  # Starting directory for directory walk

word = win32com.client.Dispatch("Word.application")

for dir_path, dirs, files in os.walk(baseDir):
    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        file_name, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == '.doc':  #
            docx_file = '{0}{1}'.format(file_path, 'x')
            if not os.path.isfile(docx_file):  # Skip conversion where docx file already exists
                print('Converting: {0}'.format(file_path))
                try:
                    wordDoc = word.Documents.Open(file_path)
                    wordDoc.SaveAs2(docx_file, FileFormat=16)
                    wordDoc.Close()
                except Exception as e:
                    print('Failed to Convert: {0} {1}'.format(file_path, e))
word.Quit()


# def get_doc_text(filepath, file):
#     if file.endswith('.docx'):
#         text = docx2txt.process(file)
#         return text
#     elif file.endswith('.DOC'):
#         # converting .doc to .docx
#         doc_file = filepath + file
#         docx_file = filepath + file + 'X'
#         if not os.path.exists(docx_file):
#             os.system('antiword ' + doc_file + ' > ' + docx_file)
#             with open(docx_file, encoding='utf-8') as f:
#                 text = f.read()
#             # os.remove(docx_file)  # docx_file was just to read, so deleting
#         else:
#             # already a file with same name as doc exists having docx extension,
#             # which means it is a different file, so we cant read it
#             print('Info : file with same name of doc exists having docx extension, so we cant read it')
#             text = ''
#         return text
#
#
# filepath = 'C:\\Users\\Ohad\\PycharmProjects\\OcrErrorDetection\\'
# files = os.listdir()
# for file in files:
#     text = get_doc_text(filepath, file)
#     print(text)
