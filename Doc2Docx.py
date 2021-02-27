import os
import win32com.client


def Doc2Docx(baseDir):
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
