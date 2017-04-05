#!/usr/bin/python
#-*- coding: UTF-8 -*-
"""
#正负数判断
a = input("请输入一个整数：")
if a > 0 :
	print "a是正整数。"
elif a == 0 :
	print "a等于零。"
else :
 print "a是负整数。"
b = raw_input("请输入一个字符串：")
"""

"""
#for循环输出字符串
i = 0
while i < len(b):
	print b[i]
	i = i + 1
"""

"""
#for输出字符串
b = raw_input("请输入一个字符串:")
for i in b:
	print i
"""

"""
#求list内数据的和
a = range(1,100,2)
b = range(2,100,2)
print a
print b
sum_a = 0
sum_b = 0
for i in a:
 sum_a = sum_a + i
print "sum_a =",sum_a
for i in b:
 sum_b = sum_b + i
print "sum_b =",sum_b
"""


#制作菜单选择程序
import sys
while True:
 print "(1) 求5个数的和"
 print "(2) 求5个数的平均值"
 print "(X) 退出"
 a = raw_input("请输入:")
 if a == '1':
  b = raw_input("请输入5个整数(用,分隔)：")
  print "求和"

 elif a == '2':
  b = raw_input("请输入5个整数(用,分隔)：")
  print "求平均值"

 elif a == 'X':
  break
 else:
  print "请输入有效的字符!!!!"
  continue
    
