def outer1(func):
	def inner(*args,**kwargs):
		print("认证成功！")
		result = func(*args,**kwargs)
		print("日志添加成功")
		return result
	return inner
def outer2(func):
	def inner(*args,**kwargs):
		print("一条欢迎信息。。。")
		result = func(*args,**kwargs)
		print("一条欢送信息。。。")
		return result
	return inner
@outer1
@outer2
def f1(name,age):
 print("%s 正在连接业务部门1数据接口......"%name)
# 调用方法
f1("jack",18) 