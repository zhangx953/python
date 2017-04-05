#!/usr/bin/python
#coding=utf-8

class Person:
	'定义员工类'
	personCount = 0
	def __init__(self, name,salary):
		self.name = name
		self.salary = salary
		Person.personCount += 1

	def displayCount(self):
		print "人类数量统计打印。"

	def displayPerson(self):
		print "Name:",self.name, "Salary:",self.salary

class Employee(Person):
	
#	def __init__(self, name,salary):
#		self.name = name
#		self.salary = salary
	
	def displayCount(self):
		print "员工人数统计打印。"

ps1 = Person("zhangx",2500)
emp1 = Employee("liming",3800)
print ps1.displayCount()
print emp1.displayCount()

print "共有人员%d" % Person.personCount,"人"

ps1.addr = "辽宁省鞍山市铁东区园林路43号"
ps1.age = 45

print getattr(ps1,'age')
