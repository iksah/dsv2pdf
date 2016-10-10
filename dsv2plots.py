import csv
import math
import argparse
import __builtin__
import matplotlib.pyplot as pyplot

parser = argparse.ArgumentParser()
parser.add_argument("func", type=str, help="function for plot")
parser.add_argument("delim", type=str, help="delimeter")
parser.add_argument("pathFrom", type=str, help="name of csv")
parser.add_argument("pathTo", type=str, help="name of pdf (without ext)")
args = parser.parse_args()

data = [];
with open(args.pathFrom, 'rb') as csvFile:
    reader = csv.reader(csvFile, delimiter=args.delim)
    for row in reader:
        data += [row]

def analize(data, function):
    headers = data[0]
    headersData = [];
    footers = [];
    for i in range(0,len(headers)):
        headersData += [[]];
        footers += [[]];
        for j in range(1,len(data)):
            headersData[i] += [float(data[j][i])]
        func = getattr(__builtin__,function)
        footers[i] = func(headersData[i])
    return [headers,headersData,footers]

plotData = analize(data,args.func)
pyplot.plot(plotData[2])
pyplot.savefig(args.pathTo+".pdf")
