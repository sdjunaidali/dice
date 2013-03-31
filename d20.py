import random

def roll20(number_of_dice):
	"""
		returns the results of rolling <number_of_dice> d20 dice in a list	
	"""
	results = []
	for i in range(1,(number_of_dice+1)):
		results.append(int(random.uniform(1,21)//1))
	return results
