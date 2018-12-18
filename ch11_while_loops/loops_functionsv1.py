#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:25:00 2018

@author: Me
"""

#x = 33
#while x >= 1:
#    print(x, ': ', end='')
#    x = x / 2
#print(x)

#COMPUTING TRIANGULAR NUMBERS

#def tri(input):
#    
##    while input > 0:
#
#    triNo = input 
#
#    print(triNo, 1)
#    
#    while sum > 1:
#        
#        if triNo > 1 and sum != :
#            sum = input - 1
#            triNo = input + sum
#            print(triNo, 2)
#        else:
#            sum = 0
#            triNo = input + sum
#            print(triNo, 'else')
#        
#    print(triNo)
#    return sum
#        
#tri(4)
#


def triangular(n):
    trinum = 0
    while n > 0:
        trinum = trinum + n
        n = n - 1
    print(trinum)
    return trinum





#BREAK

i = 55
while i > 10:
    print(i)
    i = i * 0.8
    if i == 35.2:
        break

#USER GREETING UNTIL BREAK

while True:
    name = input('Enter name: ')

    if name == 'done':    
        break
    print('Hello', name)
    

