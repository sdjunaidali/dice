import d6
import d20
import sys

while True:
        try:
                type = input("Please enter the type of die you want to roll\n(d6 or d20): ")
                num = int(input("Enter the number of die you want to roll: "))
                myResult = []
                if type == "d6":
                        print ("rolling d6s")
                        myResult = d6.SixSidedDice(num)
                elif type =="d20":
                        print ("rolling d20s")
                        myResult = d20.roll20(num)
                else:
                        print ("Invalid input")

                print (myResult)
        except ValueError:
                           print('Value error! Please try again!')
