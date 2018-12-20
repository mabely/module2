# -*- coding: utf-8 -*-

import requests
import lxml
from bs4 import BeautifulSoup

my_snacks = ['rice crackers', 'cheese crackers', 'banana', 'pears', 'mandarins']

for item in my_snacks:
    print(item)

values = [1, 3, 5]

for val in values:
    print('---->' + str(val))
    print('---->' + str(val+50))


oldsentence = 'This is my sentence'
sentence = oldsentence.split()
for word in sentence:
    print(word)

#LOOPING THROUGH A STRING - RETURNS EACH CHARACTER
for words in 'Here is another sentence':
    print(words)

#LOOPING THROUGH A TUPLE
densities = {'iron': [7.8, 14, 76], 'gold': [19.3, 364, 15], 'zinc': [7.13, 7, 7], 'lead': [11.4, 6, 83]}

metals = list(densities.keys())
densities_pairs = sorted(densities.items(), key = lambda kv : kv[1][0])
#for metal in metals:
#    print(metal, densities[metal])

#PRINTS ONLY IF INDEX POSITION 0 OF VALUES IN DENSITIES DICTIONARY ARE OVER 10
for k, v in sorted(densities.items(), key = lambda kv : kv[1][1], reverse = True):
    if v[0] > 10:        
        print(k,v)

#for metal in metals:
#    print(’{0:>8} = {1:5.1f}’.format(metal,densities[metal]))

values = [1, 3, 5]

#INCREMENTAL ADDING OF ALL NUMBERS IN LIST WITH FOR LOOP
total_count = 0

for val in values:
    total_count += val
print('TOTAL: ' + str(total_count))
    
#ANOTHER WAY TO ADD UP ALL NUMBERS IN LIST

def sum_values(l):
    sumV = 0
    for val in l:
        sumV += val
    return sumV
print(sum_values(values))


outer_vals = [1, 2, 3]
inner_vals = ['soup', 'bread', 'butter']

d = {}

for oval in outer_vals:
    if oval in d:
        print('it is there')
    else:
        for ival in inner_vals:
            d[oval] = ival
            print(d)
    


# List of strings
listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
    
# List of ints
listOfInt = [56, 23, 43, 97, 43, 102]


# Create a zip object from two lists
zipbObj = zip(listOfStr, listOfInt)

# Create a dictionary from zip object
dictOfWords = dict(zipbObj)

# Create a zip object from two lists
zipbObj = zip(listOfStr, listOfInt)
 
# Create a dictionary from zip object
dictOfWords = dict(zipbObj)

print(dictOfWords)


    

