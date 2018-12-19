# -*- coding: utf-8 -*-

from ch3file1_mabel_functions import *
from ch3file3_mabel_age_calc import hello_world

#AGE CALCULATOR FUNCTION FROM ch3file3_mabel_age_calc - USES USER INPUT TO CALCULATE AGE
hello_world()

#CALLING .FORMAT FUNCTIONS
hello_world_2args('Morning', 'Mabel')
a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
hello_world_2args(a1, b1)
hello_world_2args(a2, b2)

add_two_numbers()
add_two_numbers_from_args(5,10)

#CALLING FUNCTION BY STORING RETURNED VALUE INTO VAR
returned_dist = convert_distance(1)
print(returned_dist)

#CALLING FUNCTION WITH ARGUMENTS FROM A VAR
a=33
fahrenheit, kelvin = convert_temp(a)
print('It\'s ' + str(a) + ' celsius, but in the US they would say it\'s ' + fahrenheit)

#STORING RETURNED VALUES TO VARS
var1, var2 = convert_temp(33)
print('Now we know the temp is '+ str(var2) + ' and ' + str(var1) )

#STORING USER INPUT INTO VAR
name = input('What is your name? ')
print('Hello', name)

