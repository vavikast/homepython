def foo():
	print("我是原始函数！") 
def outer(func):
	def inner():
		print("我是内层函数！")
		return func()
	return inner

f=outer(foo)
f()
d=outer(foo())
d=outer(foo())
d


