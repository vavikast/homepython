import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('call %s():' % func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log
def now():
	print('2015-3-25')
@log('execute')
def f():
    pass
f()
print(f.__name__)