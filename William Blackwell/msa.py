#Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use an array to do this exercise
count = 0
for count in range(1,1000):
	if count % 2 == 1:
		print count	


#Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for count in range(5,1000000):
	if count % 5 == 0:
		print count


#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]		

a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b


a = [1, 2, 5, 10, 255, 3]
b = sum(a)/ len(a)
print b