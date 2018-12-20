# -*- coding: utf-8 -*-

reading_list = ['a tale of two cities', 'hunger games', 'Autobiography of Michelle Obama']
a = ['1', '2','4']
b = ['3', '6', '7']

#CREATING A LIST
x = ['shopping list', 'gift list', reading_list]
print(x)

#MODIFYING THE LIST
x[2] = 'to do list'
print(x)
x[2] = reading_list

#ACCESSING ITEMS IN LIST USING THEIR POSITION
print(reading_list[2][1])

#REMOVES ITEM IN LIST
print(x)
x.remove('shopping list')
print(x)

#APPENDING: in this instance, y becomes a none type, even if there was no 'x=y'
#as below. In that instance below, 
print(x)
y = x
y = x.append('wish list')
print(y)

#REMOVING A DUPLICATE ITEM IN LIST WILL REMOVE ONLY ONE INSTANCE
x.append('wish list')
x.append('wish list')
print(x)
x.remove('wish list')
print(x)
del x[1]

#ONLY THIS OPERATOR WORKS ON STRINGS
print(a+b)
print(a*3)

#CANNOT PERFORM THESE STRING ON STRING, ETC
#print(a-b)
#print(a*b)
#print(a/b)
#print(a+3)
#print(a+'3')

#CREATES DICTIONARY (the key)!
print(set(a+b))

#SLICING A LIST, INCLUSIVE THEN EXCLUSIVE
y = a+b
print(y)
print(y[4:10])
#THIS RETURNS NOTHING!
print(y[0:0])
#THIS CAN PRINT BUT RETURNS NOTHING AS OUT OF RANGE
print(y[-3:-6])
print(y[-3:-1])

#SORTING
y = a + b
print(sorted(y))
print(sorted(y, reverse=True))

y = a + b
y.sort()
print(y)
y.sort(reverse=True)
print(y)

t = set(a+b)
print(t)

#CREATING TUPLES, THESE ARE IMMUTABLE
z = ('this', 'and', 'that')

#LAMBDA

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["xa", "sb", "lf", "hw", "ed", "fy"]
y = sorted(x)
z = ["fg", "uj", "sx", "uj", "ww", "cf"]

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]

sorted(x2)

schedule = [('Mabel', 'Saturday', 3), ('Loren', 'Friday', 2), ('Amanda', 'Tuesday', 8)]
# SORTS BY A SPECIFIC POSITIION IN THE TUPLE
print(sorted(schedule, key=lambda s:s[2]))



