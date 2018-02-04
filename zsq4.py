def outer(func):
	print("认证成功！")
	result = func()
	print("日志添加成功")
	return result
@outer
def f1():
	print("业务部门1数据接口......")
# 业务部门并没有开始执行f1函数

f1()