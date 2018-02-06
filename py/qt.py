
def f1():
	print('f1')
def wl(func):
    def inner():
        # 验证1
        # 验证2
        print('you are right')
        return func()
    return inner
	

print(wl(f1))