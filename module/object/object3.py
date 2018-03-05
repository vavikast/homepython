#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '


__author__ = 'vavikast'
class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	
	
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self,score):
		self.__score=score
	def print_score(self):
		print('%s ' % self.__score)
bart =Student('Besll Hkee',59)
bart.ss=55
print(bart.ss)
print(bart.get_name())
print(bart.get_score())
bart.print_score()