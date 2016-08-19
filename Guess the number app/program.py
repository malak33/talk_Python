#import random
import random

print('--------------------------')
print('  Guess the number game   ')
print('--------------------------')
print()

#the_number = random.randint(0, 100)
the_number = random.randint(0, 100)
guess = -1

name = input('Player what is your name? ')

# debug
#print(guess_text, type(guess_text))
#print(guess, type(guess))

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('Sorry {1}, your guess of {0} was too LOW'.format(guess, name))
    elif guess > the_number:
        print('Sorry {1}, your guess of {0} was too HIGH'.format(guess, name))
    else:
        print('Excellent work {1}, you win! The number was {0}.'.format(guess, name))
print('done')



