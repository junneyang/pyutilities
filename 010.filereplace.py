#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        007.getfilemd5.py
# Purpose:     python获取文件md5（包括较大文件）
#
# Author:      yangjun03
#
# Created:     02/12/2014
# Copyright:   (c) yangjun03 2014
# Licence:     <The MIT License (MIT)>
#-------------------------------------------------------------------------------
import sys
import codecs
import linecache

def get_file_lines(filepath):
    try:
        lines=linecache.getlines(filepath)
        return lines
    except Exception as e:
        print(e)
    finally:
        linecache.clearcache()

if __name__ == "__main__":
    filepath = sys.argv[1]
    dst_filepath = sys.argv[2]
    firstline = None
    cntstr = ""
    lines = get_file_lines(filepath)
    for line in lines:
        firstline = line.replace("\t3\n","\t4\n")
        cntstr += firstline

    with codecs.open(dst_filepath, "w", encoding="utf-8") as fp:
        fp.write(cntstr)
