def funWith():
	for count in range(1,2001):
		if count % 2 == 0:
			print "number is {} This is an even number".format(count)

		else:
			print "number is {} This is an odd number".format(count)

print funWith()

		#muliply

def multiply(arr):

	arr = [i * 5 for i in arr]
	print arr

multiply([3,5,7,8])


