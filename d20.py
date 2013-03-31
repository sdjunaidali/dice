import random
def gen_20(number_of_dice):
	results = []
	for i in range(1,(number_of_dice+1)):
		results.append(int(random.uniform(1,21)//1))
	return results
