#-*- coding: utf-8 -*-
def generator():
	while True:
		receive=yield 1
		print('extra' +str(receive))
g=generator()
print(next(g))
print(g.send(111))

