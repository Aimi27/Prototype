import PyPDF2,textract,docx,os
from PyPDF2 import PdfFileMerger

#The uploaded filepaths
filepaths = 'insert filepath'

#seperates the file from the filepath
root,ext = os.path.split(filepaths)
def extractData(file):
    if ext.endswith('.pdf') :
        pdfFile = open(ext, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(0,pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
            Str =  str(pageObj.extractText())
            print(Str)


    elif ext.endswith('.docx'):
        print('Doc says hello')
        text = textract.process(filepaths)
        print(text)

    elif ext.endswith('.txt'):
        print('Txt says hello instead')
        f = open(ext, 'rb')
        read = f.read()
        print(read)