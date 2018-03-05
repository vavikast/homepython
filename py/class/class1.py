#-*- coding: utf-8  -*-
class Animal(object):
	def run(self):	
		print('Animal is runing:')

class Dog(Animal):
    def run(self):
        print('Dog is running')
		#pass
	#def eat(self):
		#print('Eating meat...')
	#	pass
class Cat(Animal):
	def run(self):
		print('Cating meat...')
	#pass 

dog=Dog()
dog.run()
cat=Cat()
cat.run()

