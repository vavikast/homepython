# -*- coding: utf-8 -*-
class A(object):
    def f(self):
        print("A")
class B(object):
    def f(self):
        print("B")
class C(B,A):
    pass
c = C()
c.f()
class D(A,B):
	pass
d=D()
d.f()