import d20, d6, sys

while True:
	type = raw_input("Please enter the type of die you want to roll\n(d6 or d20): ")
	num = raw_input("Enter the number of die you want to roll: ")
	print "type: ", type, "\nnumber: ", num
	exit_case = raw_input("Quit? y/n: ")
	if exit_case == "y":
		break		
	else:
		pass
