from random import randint
guesses = 6
guess_number = randint(1,10)
for guess in range(guesses):
	print ("Can you guess the number? ")
	guessed = int(input())
	if guessed < guess_number:
		print("Take a higher guess")
	elif guessed > guess_number:
		print("Take a lower guess")
	else:
		print("Correct in", guess, "attempts!")
		break
if guessed != guess_number:
	print("Sorry, you could not guess it")