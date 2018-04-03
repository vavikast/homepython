#-*- coding: utf-8  -*-
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
s=Student('Bob',20,88)
print(s())