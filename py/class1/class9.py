#-*- coding: utf-8  -*-
class Fib(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
f=Fib()
f[0]
f[1]
