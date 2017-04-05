#!/usr/bin/python
#-*- coding: utf-8 -*-

#############################
# Filename: test.py
# CreateDate: 2017-02-17
# Author: Zhangxin
# Version: V1.0.0
# Function: find keyword in 
#       string of input text
#############################

import keyword
import copy
import string

dict1 = {'name':'WangXL','age':35,'sex':'man','birthday':'1987-02-21'}
dict2 = {1:'wang',2:'li',3:'zhou',4:'lin',5:'guo'}

#i = 0
f = open('/tmp/person','ab+')
for key in dict1:
	b = str(key) + ':' + str(dict1[key])
	f.write(b)
	f.write("\t")
f.write("\n")
f.close()

f = open('/tmp/person','ab+')
for key in dict2:
	b = str(key) + ':' + str(dict2[key])
	f.write(b)
	f.write("\t")
f.write("\n")
f.close()

print dict2[1]
print dict2[2]
print dict2[3]
print dict1.keys()
print dict1.values()


