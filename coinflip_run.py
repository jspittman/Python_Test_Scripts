import random

print('Coin Flips - Press Enter')

input()

flips = 0
heads = 0

while flips < 1000:
	if random.randint(0,1) == 1:
		heads = heads + 1
	flips = flips + 1

	if flips == 900:
		print ('900 flips and there have been ' + str(heads) + ' heads.')
	if flips == 100:
		print ('At 100 tosses, heads has come up ' + str(heads) + ' times.')
	if flips == 500:
		print ('Halfway done, and heads has come up ' + str(heads) + ' times!')

print()
print('Out of 1000 coin tosses, heads comes up ' + str(heads) + ' times!')
print('Were you close?')
