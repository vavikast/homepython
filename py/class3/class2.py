# -*- coding: utf-8 -*-
def fn(self,name='world'):
	print('Hello,%s.' % name)
Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()
#1.class对象名
#2.继承父类的集合，tuple类型，上述函数表示有且只有一个对象的时候的写法。
#3.clas的方法与函数的绑定，这里是将fn函数绑定到Hello class。键对应方法名，值对应方法引用
