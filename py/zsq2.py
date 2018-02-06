
def wl(func):
    def inner():
        # 验证1
        # 验证2
        print('可以是吗')
        return func()
    return inner
 
@wl
def f1():
    print('This is no ')

	
f1()
