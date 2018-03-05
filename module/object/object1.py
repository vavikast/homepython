#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'vavikast'
class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s %s' % (self.name,self.score))
	

bart =Student('Besll Hkee',59)
bart.print_score()
