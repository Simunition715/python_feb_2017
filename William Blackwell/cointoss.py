def coin_toss():
	heads = 0
	tails = 0
	attempt = 0
	for a in range(0,5000):
		import random
		a = random.random()
		a = round(a)
		
	#for a in range(0,5000):
		if a == 0:
			heads += 1
			attempt += 1
			print "attempt {} Throwing a coin...It's a Head!...Got {} head(s) so far and {} tail(s) so far".format(attempt,heads,tails)
		elif a == 1:
			tails += 1
			attempt += 1
			print "attempt {} Throwing a coin...It's a tails!...Got {} tails(s) so far and {} heads(s) so far".format(attempt,tails,heads)


coin_toss()			