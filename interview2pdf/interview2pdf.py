#!/usr/bin/python
# -*- coding: utf-8 -*- 
import argparse

import interview2csv
import csv2pdf

parser = argparse.ArgumentParser()


parser.add_argument("pathFrom", type=str, help="путь к файлу с результатами опроса " )

parser.add_argument("-pt",  type=str,help=" путь(имя) к файлу-отчету (с раширением .pdf), по умолчанию: ./result.pdf", dest = "pathTo")

parser.add_argument("-ct", type=str, help="тип графиков для full отчетов", dest = "chartType", choices = ['pie','bar'])

parser.add_argument("-t", type=str, help=" тип данных ", dest = "type", choices = ['full','common'])

parser.add_argument("-com", help=" путь к файлу со значениями заголовков вопросов, на которые необходимо дать развернутый ответ.", dest = 'comments')

ar_pathTo = parser.parse_args().pathTo
ar_type = parser.parse_args().type
ar_chartType = parser.parse_args().chartType
ar_pathFrom = parser.parse_args().pathFrom
ar_comments = parser.parse_args().comments


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
