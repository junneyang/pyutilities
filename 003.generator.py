#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        003.generator.py
# Purpose:     如何快速实现函数可迭代？使用yield。基于yield指令，允许停止函数并立即返回结果
#              此函数保存其执行上下文，如果需要，可立即继续执行。
#
# Author:      yangjun03
#
# Created:     02/12/2014
# Copyright:   (c) yangjun03 2014
# Licence:     <The MIT License (MIT)>
#-------------------------------------------------------------------------------

def GeneratorTest():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    g = GeneratorTest()
    print [g.next() for i in xrange(10)]



