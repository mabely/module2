#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

attempts = 0
number = randint(1, 21)
    
def guess(attempts, number):
    
    while attempts <= 4:
        guess = input('(Type "quit" to exit game) \n\nGuess a number: ')
#        print(number)
        
        if guess == 'quit':
            break
        
        else:
            try:
                if int(guess) == number:
                    print('YOU GOT IT! \n\nThanks for playing!')
                elif int(guess) > number:
                    print('Too high!')
                elif int(guess) < number:
                    print('Too low!')
                
            except ValueError:
                print('Oops I did not recognise that!')
             
            attempts += 1
            print('You have made', attempts, 'out of 5 guesses')
    
    if guess == 'quit':
        print('Bye!')
    else:
        print('GAME OVER \nToo many guess, you\'ve lost :( \n\nThanks for playing!')
    
    return attempts

guess(attempts, number)






