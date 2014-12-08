#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        004.operator.py
# Purpose:     运算符重载？比较两个对象是否相等？
#
# Author:      yangjun03
#
# Created:     02/12/2014
# Copyright:   (c) yangjun03 2014
# Licence:     <The MIT License (MIT)>
#-------------------------------------------------------------------------------

class OperatorTest(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def  __cmp__(self, other):
        if(self.id == other.id and self.name == other.name):
            return 0

if __name__ == "__main__":
    #==运算符重载
    a = OperatorTest(123,"abc")
    b = OperatorTest(123,"abc")
    print a is b
    print a == b

    #lambda运算符
    g = lambda x : x**2
    print g(4)

    #基本数据类型==运算符已经重载
    a = 1
    b = 1
    print a is b
    a = "Hello"
    b = "Hello"
    print a is b
    a = [1,2,3]
    b = [1,2,3]
    print a is b
    print a == b

    #列表元素快速去重
    a = [1,2,2,3,4,4]
    print list(set(a))
    a = [1,2,2,3,4,4]
    print {}.fromkeys(a).keys()
