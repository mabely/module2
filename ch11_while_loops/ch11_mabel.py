#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#REPEATED DIVISION AND PRINTING
x = 33
while x >= 1:
    print(x, ': ', end='')
    x = x / 2
print(x)

#================================================
#COMPUTING TRIANGULAR NUMBERS
#================================================

def triangular(n):
    trinum = 0
    while n > 0:
        trinum = trinum + n
        n = n - 1
    print(trinum)
    return trinum


#================================================
#USING BREAKS IN WHILE LOOPS
#================================================
    
i = 55
while i > 10:
    print(i)
    i = i * 0.8
    if i == 35.2:
        break


#================================================
#USER GREETING UNTIL BREAK
#================================================

def userGreeting():
    
    while True:
        name = input('Enter name: ')
    
        if name == 'done':    
            break
        print('Hello', name)


#================================================
#ASSESSING GRADES V1
#================================================

grade = 1

while grade > 0:
    grade = int(input('(type "exit" to quit program) \nGo on, tell us your grades: '))
    if grade >= 70:
        print('FIRST CLASS')
    elif grade < 40:
        print('FAIL')
    elif grade >= 40:
        print('PASS')
    elif grade == 'done':
        break

#================================================
#ASSESSING GRADES V2: with exception handling
#================================================
        
def grade():
    
    while True:
        grade = input('(type "quit" to exit program) \nGo on, tell us your grades: ')
        try:
            if int(grade) >= 70:
                print('FIRST CLASS')
            elif int(grade) < 40:
                print('FAIL')
            elif int(grade) >= 40:
                print('PASS')
        
        except ValueError:
            if grade == 'exit':
                break
            else:
                print('Sorry, try again, I did not recognise that')















            