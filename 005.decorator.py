#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        005.decorator.py
# Purpose:     如何使用装饰器？装饰器其实也就是一个函数，一个用来包装函数的函数，返回一个修改之后
#              的函数对象，将其重新赋值原来的标识符
#
# Author:      yangjun03
#
# Created:     02/12/2014
# Copyright:   (c) yangjun03 2014
# Licence:     <The MIT License (MIT)>
#-------------------------------------------------------------------------------
def decoratortest(args):
    def _decoratortest(func):
        def _deco(a, b):
            print(args + " : before myfunc() called.")
            ret = func(a, b)
            print(args + " : after myfunc() called.")
            # 不需要返回func，实际上应返回原函数的返回值
            return ret
        return _deco
    return _decoratortest

@decoratortest("moduleA")
def myfunc(a, b):
    print("\tmyfunc(%s, %s) called." %(a, b))
    return a + b

a = myfunc(10, 20)
print a
a = myfunc(20, 30)
print a

import threading
mutex = threading.Lock()

def singletondeco(cls):
    instances = {}
    def getInstance():
        if cls not in instances:
            mutex.acquire()
            if cls not in instances:
                instances[cls] = cls()
            mutex.release()
        return instances[cls]
    return getInstance

@singletondeco
class SingletonClass(object):
    pass

s1 = SingletonClass()
s2 = SingletonClass()
print s1 is s2
