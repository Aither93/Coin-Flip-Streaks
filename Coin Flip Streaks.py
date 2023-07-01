import random
num_streaks = 0
for i in range(10000):
	# Code that creates a list of 100 'heads' or 'tails' values.
	flips = []
	counter = 0
	for x in range(100):
		if random.randint(0, 1) == 0:
			flips.append("H")
		else:
			flips.append("T")
	# Code that checks if there is a streak of 6 heads or tails in a row.
	for ind in range(1 , 100):
		if counter == 6 :
			num_streaks += 1
			counter = 0
		else:
			if flips[ind] == flips[ind - 1]:
				counter += 1
			else:
				counter = 0

print('Chance of streak: %s%%' % ( num_streaks/1000000))

