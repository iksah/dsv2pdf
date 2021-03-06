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
            img = plt.figure(figsize = (10, 7.5))
            # font = {'family': 'Serif',
            #         'weight': 'normal'}
            # rc('font', **font)
            if (plotType == "pie"):
		sum = 0
                for buf in record[6:]:
                    sum += int(buf)
                iter = 0
                lst = []
                lbl = []
                col = ['#00FF00', '#FFFF00', '#FF0000', '#48D1CC', '#C71585']
                for j in record[6:]:
                    iter += 1
                    if j!='0':
                        lst.append(int(j))
                        lbl.append(str(iter) + ':' + j + '(' + str(int(j) * 100 / sum) + '%)' )
                hex = col[:len(lst)]
                plt.pie(x = lst,
                        labels = lbl, colors = hex,
                        startangle = 95,pctdistance = 20,labeldistance =20)
                plt.legend(loc="best")
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
    








