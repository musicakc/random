from random import randint

repeat = True
while repeat:
	print("You rolled ", randint(1,6))
	print("Do you want to roll again? ")
	repeat = ("y" or "yes" or "Y" or "YES") in input().lower()