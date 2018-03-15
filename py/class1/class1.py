#-*- coding: utf-8  -*-
class Animal(object):
	pass
class Mammal(Animal):
	pass
class Bird(Animal):
	pass
class Dog(Mammal):
	pass
class Bat(Mammal):
	pass
class Parrot(Bird):
	pass
class Ostrich(Bird):
	pass
class Runable(object):
	def run(self):
		print('Running...')
class Flyable(object):
	def fly(self):
		print('Flying...')

