#!/usr/bin/python
# -*- coding: utf-8 -*- 
import argparse

import interview2csv
import csv2pdf

parser = argparse.ArgumentParser()
parser.add_argument("pathFrom", type=str, help="name of csv")
parser.add_argument("pathTo", type=str, help="name of pdf")
parser.add_argument("type", type=str, help="full / common", nargs='?')
parser.add_argument("chartType", type=str, help="pie / bar", nargs='?')
parser.add_argument("comments", type=str, help="file with comments", nargs='?')
args = parser.parse_args()

if (not args.chartType):
    args.chartType = 'pie'
if (not args.type):
    args.type = 'full'
if (args.comments):
    path = args.comments
    text = open(path)
    args.comments = []
    for line in text:
        args.comments += [item.strip("\n")]
    text.close()
else:
    args.comments = [u'Оставьте комментарий:']

if (args.type == 'full'):
    csvData = interview2csv.parseInterviewDataRaw(interview2csv.readDataRaw(args.pathFrom), args.comments) 
    csv2pdf = csv2pdf.csv2pdf(csvData, args.pathTo, args.chartType)
elif (args.type == 'common'):
    csvData = interview2csv.parseInterviewDataRawCommon(interview2csv.readDataRaw(args.pathFrom), args.comments) 
    csv2pdf = csv2pdf.csvCommon2pdf(csvData, args.pathTo)
