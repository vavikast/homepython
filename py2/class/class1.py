#-*- coding: utf-8  -*-
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
	    return self.__name

bart=Student('Bart Simpson',59)
print(bart.get_name())