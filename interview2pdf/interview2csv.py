#!/usr/bin/python
# -*- coding: utf-8 -*- 

import string

def readDataRaw(path):

    text = open(path)
   # print("this TEXT!!!!!!!!!!!!!!!!!!\n")
   # print(text)
    dataRaw = []
    recordRaw = []
    for line in text:
        if ((line == '\n') and (recordRaw != [])):
            dataRaw += [recordRaw]
            recordRaw = []
        elif (line != '\n'):
            recordRaw += [line.decode('utf8').split(';')]
    if recordRaw != []:
        dataRaw += [recordRaw]
        recordRaw = []
    text.close()
    return dataRaw

def parseInterviewDataRaw(dataRaw, comments=[u'Оставьте комментарий:']):
    data = [[
        u'Семестр',
        u'Направление',
        u'Преподаватель',
        u'Предмет',
        u'Вопрос',
        u'Тип ответов',
        u'Ответы']]
    record = []
    for recordRaw in dataRaw:
        record = [
            recordRaw[1][0].strip('\n'),
            recordRaw[1][1].strip('\n'),
            recordRaw[2][1].strip('\n'),
            recordRaw[2][2].strip('\n'),
            recordRaw[2][0].strip('\n')
            ]
        if (record[4] in comments):
            record += ['comment']
            answers = [answer[0].strip('\n') for answer in recordRaw[3:]]
        else:
            record += ['counter']
            answers = ['0','0','0','0','0']
            for i in range(len(recordRaw[3])):
                answers[int(recordRaw[3][i])-1] = str(int(recordRaw[4][i]))
        record += answers
        data += [record]
    return data


def parseInterviewDataRawCommon(dataRaw, comments=[u'Оставьте комментарий:']):
    data = [[
        u'Вопрос',
        u'Ответы'
        ]]
    record = []
    for recordRaw in dataRaw:
        record = [
            recordRaw[0][0].strip('\n')
            ]
        answers = [answer[0].strip('\n') for answer in recordRaw[1:]]
        record += answers
        data += [record]
    return data

def saveCsv(data,path):
    text = '';
    for record in data:
        text += ("'"+u"','".join(record).encode('utf-8').strip()+"'")
        text += '\n'
    file = open(path,'w')
    file.write(text)
    file.close()

#saveCsv(parseInterviewDataRaw(readDataRaw('results.txt')),'interview.csv')
