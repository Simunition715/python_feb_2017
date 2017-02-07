
def grade_func():

	i = 1
	for i in range(0,10):
		import random
		rannum = random.random()
		grade = rannum*100
		if grade> 89 and grade < 100:
			print "score {}; Your grade is A".format(grade)
		elif grade > 79 and grade < 90:
			print "score {}; Your grade is B".format(grade)
		elif grade > 69 and grade < 80:
			print "score {}; Your grade is C".format(grade)	
		elif grade > 59 and grade < 70:
			print "score {}; Your grade is D".format(grade)	

grade_func()