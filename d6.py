import random

def SixSidedDice(numberOfDice):
	myList = []
	i = 0
	while i < numberOfDice:
		myList.append(random.randint(1,6))
		i = i + 1
	return myList
