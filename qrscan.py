#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess
import xlrd
import chardet

def myAlign(string, length=0):
    if length == 0:
        return string
    slen = len(string)
    if(string == 'IP'):
        slen -= 1
    re = string
    if isinstance(string, str):
        placeholder = ' '
    else:
        placeholder = u'　'
    while slen < length:
        re += placeholder
        slen += 1
    return re


def sh():
    path='/home/chejian/file/sets.xlsx'
    ExcelFile=xlrd.open_workbook(path)
    sheet = ExcelFile.sheet_by_index(0)
    cols=sheet.col_values(9)

    input_val = ''
    while input_val != 'exit':
        input_val = raw_input("input:")
        os.system('clear')
        print 'get str:',input_val
        if input_val == 'exit':
            break;
        if len(input_val) <= 1:
            continue;
        
        
        linenum=0
        for value in cols:            
            if isinstance(value,float):
                value = str(value)
            if input_val==value:
                print 'find value in line:',linenum
                for i in range(0,sheet.ncols):
                    cellval = sheet.cell(linenum,i).value
                    if isinstance(cellval,str):
                        cellval = cellval.strip('\n')
                    print '\033[1;33;40m',myAlign(sheet.cell(0,i).value,7),'\033[0m',':',cellval
                break
            linenum += 1
        if linenum==sheet.nrows:
            print '\033[0;31;40m数据 ',input_val,' 不存在!\033[0m'
        else:
            print '\033[1;32;40m数据 ',input_val,' 在第 ',linenum,' 条，共有 ',sheet.nrows,' 条!\033[0m'
        
    
sh()
#sh("zbarcam --raw --prescale=120x60 /dev/video0")
#sh("zbarcam --raw --prescale=40x30 /dev/video0")

