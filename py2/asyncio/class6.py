#-*- coding: utf-8  -*-
def fn(self,name='world'):
	print('Hello,%s,' %name)
Hello=type('Hello',(object,),hello=fn)
h=Hello()
h.hello()

