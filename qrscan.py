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


def sh(command, print_msg=True):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
   
    path='/home/chejian/file/sets.xlsx'
    ExcelFile=xlrd.open_workbook(path)
    sheet = ExcelFile.sheet_by_index(0)
    cols=sheet.col_values(9)
    firstscan = -1;

    for line in iter(p.stdout.readline, b''):
        firstscan += 1
        line = line.rstrip().decode('utf8')
        #line = line.rstrip()
        linenum=0
        #cols=sheet.col_values(9)
        if(len(line) <= 1):
            continue
        #-------
        #if len(line)==(len(value)+1):
            #print 'scan:',line,'scanlen',len(line)
            #print 'excel:',value,'excellen',len(value)
        if (firstscan > 0):
            line = line[1:len(line)]
        #--------
        for value in cols:
            if isinstance(value,float):
                value = str(value)
            
            if line==value:
                print 'find value in line :' ,linenum
                for i in range(0,sheet.ncols):
                    cellval = sheet.cell(linenum,i).value
                    if isinstance(cellval,str):
                        cellval = cellval.strip('\n')
                    print '\033[1;33;40m',myAlign(sheet.cell(0,i).value,7),'\033[0m',':',cellval
                break
            linenum=linenum+1
        if linenum==sheet.nrows:
            print '\033[0;31;40m数据 ',line,' 不存在!\033[0m'
        else:
            print '\033[1;32;40m数据 ',line,' 在第 ',linenum,' 条，共有 ',sheet.nrows,' 条!\033[0m'


sh("zbarcam --raw --prescale=120x60 /dev/video0")
#sh("zbarcam --raw --prescale=40x30 /dev/video0")

