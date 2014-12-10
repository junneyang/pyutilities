#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        006.singleton.py
# Purpose:     如何用python实现线程安全的单例模式？
#
# Author:      yangjun03
#
# Created:     02/12/2014
# Copyright:   (c) yangjun03 2014
# Licence:     <The MIT License (MIT)>
#-------------------------------------------------------------------------------
import threading

class Singleton(object):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        "disable the __init__ method"
        pass
    @staticmethod
    def getInstance():
        if not Singleton.__instance:
            Singleton.__lock.acquire()
            if not Singleton.__instance:
                Singleton.__instance = object.__new__(Singleton)
                object.__init__(Singleton.__instance)
            Singleton.__lock.release()
        return Singleton.__instance

if __name__ == '__main__':
    s1 = Singleton().getInstance()
    s2 = Singleton().getInstance()
    print s1 is s2
