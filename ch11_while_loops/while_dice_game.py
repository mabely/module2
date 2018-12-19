#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:05:01 2018

@author: Me
"""
from random import randint

def dice_game():
    
    while True:
        user_input = input('(Type "quit" to exit game) \n\nWill the dice throws be odd or even? ')
        dice_throw1 = randint(0, 7)
        dice_throw2 = randint(0, 7)
        dice_sum = dice_throw1 + dice_throw2
        print('First dice throw: ', dice_throw1)
        print('Second dice throw: ', dice_throw2)
        
        result_dice = dice_sum % 2
        
        if user_input == 'odd' and result_dice == 1:
            print('YOU WIN!')    
        elif user_input == 'even' and result_dice == 0: 
            print('YOU WIN!')  
        elif user_input == 'quit':
            break
        else:
            print('Sorry, YOU LOSE!')

dice_game()
