#!/usr/bin/env python3

#-*- coding: utf-8 -*-
import doctest
def ceshi(x):
    """#这是文档测试的内容
    >>> ceshi(2)
    1
    >>> ceshi(3)
    0
    """#End
    if x%2==0:
        return 1
    else:
        return 0
if __name__ == "__main__":    doctest.testmod(verbose=True) 
		