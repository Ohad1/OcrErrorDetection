import zipfile
import win32com.client
import os
import docx2txt
# import textract

baseDir = 'C:\\Users\\Ohad\\PycharmProjects\\OcrErrorDetection\\'  # Starting directory for directory walk

# filename = os.path.join(baseDir, "416226.DOCx")
my_text = docx2txt.process("416226.DOCx")
lines = my_text.split('\n\n')

for line in lines:
    print(line)
print(len(lines))

# print(type(my_text))
# print(my_text)

