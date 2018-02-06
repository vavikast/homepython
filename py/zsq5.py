def f1():
	print("业务部门1数据接口......")
def outer(func):
	print("认证成功！")
	result = func()
	print("日志添加成功")
	return result

outer(f1)
