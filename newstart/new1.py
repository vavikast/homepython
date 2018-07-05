#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
	try:
		a=int(input('输入一个整数：')) #判断输入是否为整数
	except ValueError: #不是纯数字需要重新输入
		print("输入的不是整数！")
		continue
	if int(a):
		c =int(a)%2
		if c==0:
			print("%a 是一个偶数" % a)
		else:
			print("%a 是一个奇数" % a) 
		break