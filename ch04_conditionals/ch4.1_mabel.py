# -*- coding: utf-8 -*-

#TAKING USER INPUT NUMBER AS ARGUMENTS TO PRINT WHETHER THE NUMBER IS ODD OR EVEN USING CONDITIONALS
#EXERCISE FROM https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

number = int(input('Please enter a number: '))

if number%2 == 0:
    print('This is even')

else:
    print('This is odd')


# TAKES ANOTHER USER INPUT NUMBER TO COMPARE WHETHER THE FIRST NUMBER FROM ABOVE 
# DIVIDES INTO THE LATTER
    
def oddoreven():
    number = input('Enter a number: ')
    number = int(number)

    if (number%2==0) and (number%4==0):
        print('That\'s an even number and multiple of 4!')
    
    elif number%4==0:
        print('That\'s an even number')
        
    else:
        print('That\'s an odd number')

    return number 

def oddoreven2(number):
    check = number
    num = input('Enter another number: ')
    if int(check)%int(num)==0:
        print(str(check) + ' divides evenly into ' + str(num))
    
    else:
        print(str(check) + ' doesn\'t divide evenly into ' + str(num))

my_number = oddoreven()     
oddoreven2(my_number)
