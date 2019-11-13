#import Imports as Imports
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import PyPDF2,textract,docx,os
from PyPDF2 import PdfFileMerger

#Imports the Google Cloud client library
# from google.cloud import language
# from google.cloud.language import enums
# from google.cloud.language import types

# Libraries essential to produce a word cloud
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage(location='C:/Users/AS/PycharmProjects/test2/media')
        fs.save(uploaded_file.name, uploaded_file)
        str = extractData(fs.base_location + '/' + uploaded_file.name)
        produceWordCloud(str)
    return render(request,'upload.html')


def extractData(fileLocation):
    root, ext = os.path.split(fileLocation)
    if ext.endswith('.pdf'):
        pdfFile = open(fileLocation, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
            Str = str(pageObj.extractText())
            return Str


    elif ext.endswith('.docx'):
        text = textract.process(fileLocation)
        return text

    elif ext.endswith('.txt'):
        f = open(fileLocation, 'r')
        read = f.read()
        return read

def produceWordCloud(Str):
    wordCloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(Str)
    plt.figure()
    plt.imshow(wordCloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()