#!/usr/bin/env python
#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        001.usingwith.py
# Purpose:     with的内部原理是什么？定义类，实现类的__enter__、__exit__方法即可，
#              __enter__的返回值赋给as之后的变量，__exit__方法自动执行、做一些清理工作，
#              可以控制是否抛出with部分的异常，返回True，不抛出异常；False，抛出异常
#
# Author:      yangjun03
#
# Created:     02/12/2014
# Copyright:   (c) yangjun03 2014
# Licence:     <The MIT License (MIT)>
#-------------------------------------------------------------------------------
import sys
import codecs

def getfileStr(filepath):
    cntstr = ""
    try:
        with codecs.open(filepath, "r", encoding="utf-8") as fp:
            for line in fp:
                cntstr += line
    except Exception as e:
        print(e)
    finally:
        return cntstr

class WithTest(object):
    def __enter__(self):
        print("enter")
        return 1
    def __exit__(self,*args):
        print("exit")
        return True

if __name__ == "__main__":
    filepath = sys.argv[1]
    cntstr = getfileStr(filepath)
    print cntstr

    with WithTest() as t:
        print("t is not the result of test(), it is __enter__ returned")
        print("t is 1, yes, it is {0}".format(t))
        raise NameError("Hi there")
        sys.exit()
        print("Never here")
