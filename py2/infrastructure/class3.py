#-*- coding: utf-8  -*-
while True:
	try:
		x=int(input("Please enter a number:"))
		break
	except ValueError:
		print("oops,that was no valid nuber.Please try again")
