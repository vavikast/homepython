#! -*- coding: utf-8 -*-
class A(object):
	def run(self):
		print("this class A")
class B(A):
	pass
class C(B):
	pass
test_b=B()
test_c=C()
test_b.run()
test_c.run()
