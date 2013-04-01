import d20, d6, sys

while True:
	type = raw_input("Please enter the type of die you want to roll\n(d6 or d20): ")
	num = raw_input("Enter the number of die you want to roll: ")
	if type == "d6":
		result = SixSidedDice(num)
	elif type =="d20":
		result = roll20(num)
	else:
		print "Invalid input"
	if(len(result) != 0):
		print("The dices are: ")
		for item in result:
			print str(item)
