def hello_world_2args(first, second):
    print ('{} {}'.format(first, second))
    
a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
hello_world_2args(a1, b1)
hello_world_2args(a2, b2)

#Task 3
print(list(range (10))) #Stop: Prints sequence from 0 to 10 (not incl)
print(list(range (1, 10))) #Start, stop: Prints sequence from 1-10(not incl 10)
print(list(range (1, 10, 3))) #Start, stop, step: Prints sequence from 1-10 in steps of 3

#Midclass challenge
def convert_distance(miles):
    km = (miles*8)/5.0
    print('Miles converted to kilometres:')
    print('Distance in miles: ', miles)
    print('Distance in kilometres:', km)
    return km

returned_dist = convert_distance(1)
print(returned_dist)

#Task 4
def convert_temp(centigrade):
    fahrenheit = centigrade*9.0/5.0+32
    kelvin = centigrade +273.15
#    print('Converting from centigrade to kelvin and fahrenheit')
#    print('Centigrade:', centigrade)
#    print('Fahrenheit:', fahrenheit)
#    print('Kelvin:', kelvin)
    return (str(fahrenheit)+"fahrenheit", kelvin)

var1, var2 = convert_temp(33)
print('Now we know the temp is '+ str(var2) + ' kelvin')

