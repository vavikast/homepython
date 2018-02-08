#-*- coding: utf-8  -*-
class Animal(object):
	def run(self):	
		print('Animal is runing:')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
		#pass
	#def eat(self):
		#print('Eating meat...')
	#	pass
class Cat(Animal):
	def run(self):
		print('Cating meat...')
	#pass 
def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())