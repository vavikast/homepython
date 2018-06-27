#! -*- coding: utf-8 -*-
def gen():
    for i in range(10):
        x = yield i
        print(x)
g=gen()
print(g.send(None))
print(g.send(2))
