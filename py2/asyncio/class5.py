#! -*- coding: utf-8 -*-
def G():
    i = 0
    while True:
        m = yield i
        print("m = ", m)
        i+=1
        if i > 100:break

a = G()    # 并没有执行函数体哦
print(a.send(None))  # 说好的有非None赋值
print(a.send(7))   # Output： 0 （对，实际会报错，可我们在假设呀）
print(a.send(4))   # Output： m = 4    1

