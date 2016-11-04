#!/usr/bin/python
# -*- coding: utf-8 -*- 

from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import rc
import cStringIO
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont  
import csv
# -*- coding: utf-8 -*-


def csv2pdf(data, path="result.pdf", plotType = "pie"):
    if (len(data) < 1):
        print "No data to create pdf"
    c = canvas.Canvas(path, pagesize = A4)
    pdfmetrics.registerFont(TTFont('Free Serif', 'FreeSerif.ttf'))
    c.setFont("Free Serif", 30)
    c.drawString(100, 400, u'РЕЗУЛЬТАТЫ ОПРОСА')
    c.showPage()
    headers = data[0]
    for record in data[1:]:
        c.setFont("Free Serif", 14)
        c.drawString(27, 750, headers[0]+ ' : ' + record[0])
        c.drawString(27, 720, headers[1]+ ' : ' + record[1])
        c.drawString(27, 690, headers[2]+ ' : ' + record[2])
        c.drawString(27, 660, headers[3]+ ' : ' + record[3])
        c.drawString(27, 630, headers[4]+ ' : ' + record[4])
        if record[5]=='comment':
            y = 600
            for comment in record[6:]:
                c.drawString(27, y, '    ' + comment)
                y -= 30
        else:
            img = plt.figure(figsize = (6, 4.5))
            # font = {'family': 'Serif',
            #         'weight': 'normal'}
            # rc('font', **font)
            if (plotType == "pie"):
                plt.pie(x = [int(dig) for dig in record[6:]],
                    labels = [
                        '1 : '+record[6],
                        '2 : '+record[7],
                        '3 : '+record[8],
                        '4 : '+record[9],
                        '5 : '+record[10
                    ]],
                    startangle = 95,
                    autopct = '%1.1f%%')
                plt.legend()
            elif (plotType == "bar"):
                bins = [1,2,3,4,5]
                plt.bar(bins, [int(dig) for dig in record[6:]], color = 'red')
                plt.grid(True)
            else:
                return
            imgdata = cStringIO.StringIO()
            img.savefig(imgdata, format = 'png')
            imgToIns = ImageReader(imgdata)
            c.drawImage(imgToIns, 27, 200, 400,400)
            img.clf()
        c.showPage()
    c.save()

def csvCommon2pdf(data, path="result.pdf"):
    if (len(data) < 1):
        print "No data to create pdf"
    c = canvas.Canvas(path, pagesize = A4)
    pdfmetrics.registerFont(TTFont('Free Serif', 'FreeSerif.ttf'))
    c.setFont("Free Serif", 30)
    c.drawString(100, 400, u'РЕЗУЛЬТАТЫ ОПРОСА')
    c.drawString(120, 300, u'(общие вопросы)')
    c.showPage()
    headers = data[0]
    for record in data[1:]:
        c.setFont("Free Serif", 14)
        c.drawString(27, 750, record[0])
        y = 720
        for comment in record[1:]:
            c.drawString(27, y, '    ' + comment)
            y -= 30
        c.showPage()
    c.save()

#path = 'interview.csv'
#text = open(path)
#dataRaw = []
#recordRaw = []
#for line in text:
#    if (line!= '\n'):
#        reader = csv.reader([line], delimiter=',', quotechar="'")
#        dataRaw += [[item.strip("' ").decode('utf8') for item in row] for row in reader]
#text.close()
#csv2pdf(dataRaw, "result.pdf", "bar")






