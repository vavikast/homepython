#! -*- coding: utf-8 -*-
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
a = consumer()    # 并没有执行函数体哦
print(a.send(None))  # 说好的有非None赋值
print(a.send(4))


