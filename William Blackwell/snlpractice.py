str = "If monkeys like bananas, then I must be a monkey!"
print str.find("monkey")
print str.replace("monkey", "alligator")


x = [2,54,-2,7,12,98]
print min(x)
print max(x)


x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]


x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
newlist = []
for i in x[:]:
	print i
	if i < 0:
		newlist.append(i)
		x.remove(i)
print newlist
x.insert(0,newlist)
print x


