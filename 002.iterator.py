#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        002.iterator.py
# Purpose:     如何实现可迭代类？定义类，并且实现该类的next、__iter__方法即可.
#
# Author:      yangjun03
#
# Created:     02/12/2014
# Copyright:   (c) yangjun03 2014
# Licence:     <The MIT License (MIT)>
#-------------------------------------------------------------------------------

class IteratorTest(object):
    def __init__(self,step):
        self.step = step
    def next(self):
        if(self.step == 0):
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        return self

if __name__ == "__main__":
    for item in IteratorTest(10):
        print item
