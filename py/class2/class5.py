#!/usr/bin/env python3

#-*- coding: utf-8 -*-
try:
	print('try...')
	r =10/int('a')
	print('result:',r)
except Exception as e:
	print('Exception',e)
except ValueError as e:
	print('ValueError',e)	
else:
	print('no error')
finally:
	print('finally...')
print('End')