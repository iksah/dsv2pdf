#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
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

def parsemng(db, collection, surname, subject,speciality, mark):
    c = MongoClient()
    try:
        c.admin.command('ismaster')
    except ConnectionFailure:
        print("Сервер монго недоступен")
        raise SystemExit
    data =[]
    xc = []
    yc = []
    db = c.get_database(db)
    col = db[collection]
    if(surname != '' and subject != '' and speciality != ''):
        for doc in col.find({'teacher' : surname, 'subject' : subject}):
            xc.append(int(doc['year']))
            buf = doc['answers']
            yc.append(int(buf[mark]))
    if(surname != '' and subject == '' and speciality != ''):
        for doc in col.find({'teacher' : surname, 'speciality' : speciality }):
            xc.append(int(doc['year']))
            buf = doc['answers']
            yc.append(int(buf[mark]))
    if(surname != '' and subject == '' and speciality == ''):
        for doc in col.find({'teacher' : surname}):
            xc.append(int(doc['year']))
            buf = doc['answers']
            yc.append(int(buf[mark]))
    data.append(yc)
    return data

def draw(db, collection,surname ='', subject ='', speciality = '', path="dynamic.pdf"):
    c = canvas.Canvas(path, pagesize = A4)
    a = parsemng(db, collection,surname, subject, speciality, '1')[0]
    if len(a) <= 0:
        print 'data not found'
    else:
        begin = a[0]
        end = a[len(a) - 1]
        c.drawString(150, 740, 'Отображена динамика за '+ str(begin) + '-' + str(end) + ' год')
        c.drawString(150, 710, 'Имя преподователя:' + surname)
        c.drawString(150, 680, 'Предмет:' + subject)
        c.drawString(150, 650, 'Специальность:' + speciality)
        img = plt.figure(figsize = (11, 11))
        for i in ['1', '2', '3', '4', '5']:
            plt.plot(parsemng(db, collection,surname, subject, speciality, i)[0],parsemng(db, collection,surname, subject, i)[1], 'ro')
            plt.plot(parsemng(db, collection,surname,
                              subject,speciality, i)[0],parsemng(db, collection,surname, subject, i)[1],
                      linewidth = 3, label = 'mark:' + i)
        plt.axis([2010, 2020, 0, 50])
        plt.xlabel(r'Years') 
        plt.ylabel(r'Marks quantit') 
        plt.legend(loc="best")
        plt.grid(True)
        imgdata = cStringIO.StringIO()
        img.savefig(imgdata, format = 'png')
        imgToIns = ImageReader(imgdata)
        c.drawImage(imgToIns, 50, 100, 500,500)
        img.clf()
        c.save()
    

draw('test','tree','Иванов Р.Г.','Программирование', 'program engineering','dinamic2.pdf')
