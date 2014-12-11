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

if __name__ == "__main__":
    filepath = sys.argv[1]
    firstline = None
    with codecs.open(filepath, "r", encoding="utf-8") as fp:
        for line in fp:
            firstline = line.strip()
            break
    firstline_list = firstline.split("\t")
    print("total fields : " + str(len(firstline_list)))
    for line in firstline_list:
        print line

