#-*- coding: utf-8  -*-
import re
test=input()
if re.match(r'\d{4}\-\w{3,7}',test):
	print('ok')
else:
	print('failed')