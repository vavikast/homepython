#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack',23,city='Beijing',addr='chaoyang',zipcode=12323)