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
import md5
import sys

def getfilemd5(filepath):
    with open(filepath, "rb") as fp:
        m = md5.new()
        while True:
            cnt = fp.read(1024)
            if not cnt:
                break
            m.update(cnt)
        return m.hexdigest()

if __name__ == "__main__":
    filepath = sys.argv[1]
    m = getfilemd5(filepath)
    print(m)

