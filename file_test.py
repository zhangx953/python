#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

of = open('ssq.txt','r')
print of.read(26)
print "当前文件位置为：",of.tell()
print of.read(15)
print "当前文件位置为：",of.tell()
of.close()

print os.getegid() 
# print "os模块包涵的函数有:",dir(os)
