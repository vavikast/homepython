# -*- coding: utf-8 -*-
def log(func):
	def wrapper(*arg,**kw):
		print ('Start %s' % func)
		return func(*arg,**kw)
	return wrapper
@log
def func_a(arg):
	pass
	
