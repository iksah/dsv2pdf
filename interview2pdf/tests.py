#!/usr/bin/python
# -*- coding: utf-8 -*- 

import filecmp

import interview2csv
import csv2pdf

def test_parseInterviewDataRaw():
    #asset
    data = [[[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'2', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'3', u'2', u'5', u'4 \xa0\n'], [u'7', u'1', u'15', u'3 \xa0\n']], [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'2', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'3', u'2', u'5', u'4 \xa0\n'], [u'7', u'1', u'15', u'3 \xa0\n']], [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'4', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'3', u'2', u'5', u'4', u'2 \xa0\n'], [u'7', u'12', u'15', u'3', u'6 \xa0\n']], [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'4', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'3', u'2', u'5', u'1 \xa0\n'], [u'7', u'1', u'15', u'1 \xa0\n']], [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'2', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'3', u'2', u'5', u'4 \xa0\n'], [u'7', u'1', u'15', u'3 \xa0\n']], [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'2', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'3', u'2', u'5', u'4 \xa0\n'], [u'7', u'1', u'15', u'3 \xa0\n']], [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'3', u'2', u'5', u'4', u'2 \xa0\n'], [u'7', u'12', u'15', u'3', u'6 \xa0\n']], [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'3', u'2', u'5', u'1 \xa0\n'], [u'7', u'1', u'15', u'1 \xa0\n']], [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \n'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b\n'], [u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \n'], [u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04390 \xa0\n'], [u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04391 \n'], [u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04392 \n'], [u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04393 \n']]]
    comments = [u'Оставьте комментарий:', u'Ответы:']
    #act
    result = interview2csv.parseInterviewDataRaw(data)
    result_comments = interview2csv.parseInterviewDataRaw(data,comments)
    #assert
    expect = [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', u'\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c', u'\u041f\u0440\u0435\u0434\u043c\u0435\u0442', u'\u0412\u043e\u043f\u0440\u043e\u0441', u'\u0422\u0438\u043f \u043e\u0442\u0432\u0435\u0442\u043e\u0432', u'\u041e\u0442\u0432\u0435\u0442\u044b'], [u'2', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'2', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'4', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '6', '7', '3', '15'], [u'4', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '1', '1', '7', '0', '15'], [u'2', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'2', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '6', '7', '3', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '1', '1', '7', '0', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:', 'comment', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04390 \xa0', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04391 ', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04392 ', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04393 ']]
    expect_comments = [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', u'\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c', u'\u041f\u0440\u0435\u0434\u043c\u0435\u0442', u'\u0412\u043e\u043f\u0440\u043e\u0441', u'\u0422\u0438\u043f \u043e\u0442\u0432\u0435\u0442\u043e\u0432', u'\u041e\u0442\u0432\u0435\u0442\u044b'], [u'2', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'2', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'4', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '6', '7', '3', '15'], [u'4', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '1', '1', '7', '0', '15'], [u'2', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'2', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '6', '7', '3', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '1', '1', '7', '0', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:', 'comment', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04390 \xa0', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04391 ', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04392 ', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04393 ']]
    compare = ((result == expect) and (result_comments == expect_comments))
    return compare

def test_parseInterviewDataRawCommon():
    #asset
    data = [[[u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04391\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 11\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 12\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 13\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 14\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 15\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 16\n']], [[u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04392 \n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 21\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 22\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 23\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 24\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 25\n'], [u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 26']]]
    #act
    result = interview2csv.parseInterviewDataRawCommon(data)
    #assert
    expect = [[u'\u0412\u043e\u043f\u0440\u043e\u0441', u'\u041e\u0442\u0432\u0435\u0442\u044b'], [u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04391', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 11', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 12', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 13', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 14', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 15', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 16'], [u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04392 ', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 21', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 22', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 23', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 24', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 25', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 26']]
    compare = (result == expect)
    return compare

def test_csv2pdf():
    #asset
    data = [[u'\u0421\u0435\u043c\u0435\u0441\u0442\u0440', u'\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435', u'\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c', u'\u041f\u0440\u0435\u0434\u043c\u0435\u0442', u'\u0412\u043e\u043f\u0440\u043e\u0441', u'\u0422\u0438\u043f \u043e\u0442\u0432\u0435\u0442\u043e\u0432', u'\u041e\u0442\u0432\u0435\u0442\u044b'], [u'2', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'2', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'4', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '6', '7', '3', '15'], [u'4', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '1', '1', '7', '0', '15'], [u'2', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'2', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '1', '7', '3', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u0418\u0432\u0430\u043d\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '0', '6', '7', '3', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u043f\u043e \u0448\u043a\u0430\u043b\u0435 \u043e\u0442 1 \u0434\u043e 5:', 'counter', '1', '1', '7', '0', '15'], [u'4', u'\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u044b', u'\u041f\u0435\u0442\u0440\u043e\u0432 \u0410.\u0412.', u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ', u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:', 'comment', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04390 \xa0', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04391 ', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04392 ', u'\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04393 ']]
    result = 'test/result.pdf'
    #act
    csv2pdf.csv2pdf(data, result, "pie")
    #assert
    expect = 'test/expect.pdf'
    return 'Please compare '+result+' and '+expect+'.'

def test_csvCommon2pdf():
    #asset
    data = [[u'\u0412\u043e\u043f\u0440\u043e\u0441', u'\u041e\u0442\u0432\u0435\u0442\u044b'], [u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04391', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 11', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 12', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 13', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 14', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 15', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 16'], [u'\u041e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u04392 ', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 21', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 22', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 23', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 24', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 25', u'\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 26']]
    result = 'test/result_common.pdf'
    #act
    csv2pdf.csvCommon2pdf(data, result)
    #assert
    expect = 'test/expect_common.pdf'
    return 'Please compare '+result+' and '+expect+'.'

print test_parseInterviewDataRaw()
print test_parseInterviewDataRawCommon()
print test_csv2pdf()
print test_csvCommon2pdf()
print '\nPress any key'
raw_input()
