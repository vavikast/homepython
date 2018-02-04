def outer(func):
	def inner():
		print('我是内层函数')
	return inner
def foo():
	print('我是原始函数')
outer(foo)
outer(foo())
outer('我是原始函数1')