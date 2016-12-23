#!/usr/bin/python
# -*- coding: utf-8 -*- 
import argparse

import interview2csv
import csv2pdf
import pr4

parser = argparse.ArgumentParser(description='Если выбрано построение динамики, обязательными являются аргументы: -bd;-col;' + 
							'и один или несколько из аргументов -sur;-sub;-mar;\n'+
						'Иначе обязательным является аргумент только -pf')

parser.add_argument("-it", type=str, help=' Тип входных данных (m - динамика  по годам (mongo), '+
							'c - визуализировать результаты опроса (csv))' ,
						 dest = "in_type", choices = ['m','c'])

parser.add_argument("-bd", type=str, help="название базы данных", dest = "db" )
parser.add_argument("-col", type=str, help="называние коллекции", dest = "collection" )
parser.add_argument("-sur", type=str, help="имя преподователя", dest = "sur" )
parser.add_argument("-sub", type=str, help="название предмета", dest = "sub" )
parser.add_argument("-mar", type=str, help="название направления", dest = "mar" )


parser.add_argument("-pf", type=str, help="путь к файлу с результатами опроса ", dest = "pathFrom" )

parser.add_argument("-pt",  type=str,help=" путь(имя) к файлу-отчету (с раширением .pdf), по умолчанию: ./result.pdf", dest = "pathTo")

parser.add_argument("-ct", type=str, help="тип графиков для full отчетов", dest = "chartType", choices = ['pie','bar'])

parser.add_argument("-t", type=str, help=" тип данных ", dest = "type", choices = ['full','common'])

parser.add_argument("-com", help=" путь к файлу со значениями заголовков вопросов, на которые необходимо дать развернутый ответ.", dest = 'comments')
ar_in_type = parser.parse_args().in_type
if (ar_in_type is None):
		print parser.print_help()
		raise SystemExit
if (ar_in_type == 'm'):

	ar_db = parser.parse_args().db
	if (ar_db is None):
		print 'Не введён аргумент названия базы данных'
		raise SystemExit
	ar_collection = parser.parse_args().collection
	if (ar_collection is None):
		print 'Не введён аргумент названия коллекции'
		raise SystemExit
	ar_sur = parser.parse_args().sur
	ar_sub = parser.parse_args().sub
	ar_mar = parser.parse_args().mar
	ar_pathTo = parser.parse_args().pathTo
	pr4.draw(ar_db,ar_collection,ar_sur,ar_sub, ar_mar,ar_pathTo)
else:
	ar_pathTo = parser.parse_args().pathTo
	ar_type = parser.parse_args().type
	ar_chartType = parser.parse_args().chartType
	ar_pathFrom = parser.parse_args().pathFrom
	ar_comments = parser.parse_args().comments

	if (ar_pathFrom is None):
		print 'Не введён аргумент пути импорта'
		raise SystemExit
	if (ar_pathTo is None):
		ar_pathTo = 'result.pdf'
	if (ar_chartType is None):
		ar_chartType = 'pie'
	if (ar_type is None):
		ar_type ='full'

	if not (ar_comments is None):
		path = ar_comments
		text = open(path)
		ar_comments = []
		for line in text:
			if line!='\n':
				ar_comments += [line.decode('utf8').strip("\n'")]
		text.close()
	else:
		ar_comments = [u'Оставьте комментарий:']
	if (ar_type == 'full'):
		csvData = interview2csv.parseInterviewDataRaw(interview2csv.readDataRaw(ar_pathFrom), ar_comments) 
		csv2pdf = csv2pdf.csv2pdf(csvData ,ar_pathTo, ar_chartType)
	elif (ar_type == 'common'):
		csvData = interview2csv.parseInterviewDataRawCommon(interview2csv.readDataRaw(ar_pathFrom), ar_comments)
		csv2pdf = csv2pdf.csvCommon2pdf(csvData,ar_pathTo)
