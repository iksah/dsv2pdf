#!/usr/bin/python
# -*- coding: utf-8 -*- 
import argparse

import interview2csv
import csv2pdf

helpTxt = "\n"
helpTxt += "interview2pdf converter \n"
helpTxt += "please, provide to script following params \n"
helpTxt += "(in any order | pattern: param=value | value without quotas) \n \n"
helpTxt += "	pathFrom - path to interview file, !required \n \n"
helpTxt += "	pathTo - path+name to pdf file, default: ./result.pdf \n \n"
helpTxt += "	type - 'common' for data with common questions \n 		or 'full' for data with questions about disciplines, optional, default: full. \n \n"
helpTxt += "	comments - path to file with comment-questions labels, optional, default: full. \n \n"

parser = argparse.ArgumentParser()
parser.add_argument("args", type=str, help=helpTxt, nargs='*')
argsN = parser.parse_args()
args = {}
for arg in argsN.args:
	arg = arg.split('=')
	args[arg[0]]=arg[1]
if not('pathFrom' in args):
	print helpTxt
else:
	if not('pathTo' in args):
		args['pathTo'] = 'result.pdf'
	if not('chartType' in args):
		args['chartType'] = 'pie'
	if not('type' in arg):
		args['type'] = 'full'
	if ('comments' in args):
		path = args['comments']
		text = open(path)
		args['comments'] = []
		for line in text:
			if line!='\n':
				args['comments'] += [line.decode('utf8').strip("\n'")]
		text.close()
	else:
		args['comments'] = [u'Оставьте комментарий:']

	if (args['type'] == 'full'):
		csvData = interview2csv.parseInterviewDataRaw(interview2csv.readDataRaw(args['pathFrom']), args['comments']) 
		csv2pdf = csv2pdf.csv2pdf(csvData, args['pathTo'], args['chartType'])
	elif (args['type'] == 'common'):
		csvData = interview2csv.parseInterviewDataRawCommon(interview2csv.readDataRaw(args['pathFrom']), args['comments']) 
		csv2pdf = csv2pdf.csvCommon2pdf(csvData, args['pathTo'])
