import random

def SixSidedDice(numberOfDice):
	"""
		returns the results of rolling <number_of_dice> d6 dice in a list	
	"""
	
	myList = []
	i = 0
	while i < numberOfDice:
		myList.append(random.randint(1,6))
		i = i + 1
	return myList
