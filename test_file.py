#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

try:
	filename = raw_input('请输入打开的文件名:')
	f = open(filename,'r')
	allLines = f.readlines()
	f.close()
except IOError:
	print "您输入的文件名不存在！"
	exit()
for eachLine in allLines:
	print eachLine

