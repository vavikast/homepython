# -*- coding: utf-8 -*-
def move(n, a, buffer, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(1,"A","B","C")
        move(n-1,"A","C","B")
        move(n+1,"C","A","B")
n=input("sdfsfsfsdf")
move(int(n),"A","B","C")