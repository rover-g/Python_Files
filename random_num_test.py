import random

print('What is you name')
name = input()

secretnumber = random.randint(1,20)

print('Hi ' + name + ' I am thinking of a number y dont you guess it')

for guesstaken in range(1, 6):
	print('Take a guess')
	guessnumber = int(input())

	if guessnumber < secretnumber:
		print('your guess is to low')
	elif guessnumber > secretnumber:
		print('your guess is too high')
	else:
		break
		
if guessnumber == secretnumber:
	print('congratulations ! you have guessed coorect number in ' + str(guesstaken) + ' guesses')
else:
	print('Try next time, Good Luck !, the number i guessed is ' +str(secretnumber))
