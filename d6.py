def SixSidedDice(numberOfDice):
	myList = []
	i = 0
	while i < numberOfDice:
		myList.append(random.randint(1,6))
		print str(myList[i])
		i = i + 1