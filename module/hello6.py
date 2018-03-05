class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def get_grade(self):
        if self.score >= 90:
			#print('yes you are a')
            return 'A'
        elif self.score >= 60:
			#print('yes you are b')
            return 'B'
        else:
			#print('yes you are c')
            return 'C'
bart = Student('Bart Simpson', 59)
bart.print_score()
bart.get_grade()