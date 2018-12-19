# -*- coding: utf-8 -*-

#.FORMAT FUNCTIONS
def hello_world_2args(first, second):
    print ('{} {}'.format(first, second))
    print(2+2)

def add_two_numbers():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer))

def add_two_numbers_from_args(number1, number2):
   answer = number1 + number2
   print ("{} plus {} is {}".format(number1, number2, answer))

#DISTANCE CONVERSION FUNCTION
def convert_distance(miles):
    km = (miles*8)/5.0
    print('Miles converted to kilometres:')
    print('Distance in miles:' , miles)
    print('Distance in kilometres:', km)
    return km

#TEMPERATURE CONVERSION FUNCTION
def convert_temp(centigrade):
    fahrenheit = centigrade*9.0/5.0+32
    kelvin = centigrade +273.15
#    print('Converting from centigrade to kelvin and fahrenheit')
#    print('Centigrade:', centigrade)
#    print('Fahrenheit:', fahrenheit)
#    print('Kelvin:', kelvin)
    return (str(fahrenheit)+" fahrenheit", str(kelvin)+" kelvin")

#RANGE FUNCTION PRACTICE 
print(list(range (10))) #Stop: Prints sequence from 0 to 10 (not incl)
print(list(range (1, 10))) #Start, stop: Prints sequence from 1-10 (not incl 10)
print(list(range (1, 10, 3))) #Start, stop, step: Prints sequence from 1-10 in steps of 3
