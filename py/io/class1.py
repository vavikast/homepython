#-*- coding: utf-8  -*-

try:
	f =open('e:\python\py\io\class1.py','r')
	print(f.read())
finally:
	if f:
		f.close()