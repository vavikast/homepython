
def product(*numbers):
	s = 1
	if len(numbers) == 0:
		raise TypeError
	else:
		for a in numbers:
			s = s * a    
		return s