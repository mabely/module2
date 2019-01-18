# -*- coding: utf-8 -*-

#LOOPING THROUGH A LIST

my_snacks = ['rice crackers', 'cheese crackers', 'banana', 'pears', 'mandarins']

for item in my_snacks:
    print(item)

#UPDATING LIST VALUES
values = [1, 3, 5]

for val in values:
    print('---->' + str(val))
    print('---->' + str(val+50))

#LOOPING THROUGH A STRING - RETURNS EACH CHARACTER
for words in 'Here is another sentence':
    print(words)

#LOOPING THROUGH A TUPLE
bt_further_tuple = ('chen','joke','rowan','lou')
bt_further_list = []
for i in bt_further_tuple:
    bt_further_list.append(i)
print(bt_further_list)

#LOOPING THROUGH A DICT
customer_data = {'name':'celine dion', 'age':55, 'gender':'female','occupation':'singer'}
value_list = []
for var in customer_data:
    #appends the values to a new list value_list    
    value_list.append(customer_data[var])
print(value_list)

#SORTING THROUGH A DICTIONARY
densities = {'iron': [7.8, 14, 76], 'gold': [19.3, 364, 15], 'zinc': [7.13, 7, 7], 'lead': [11.4, 6, 83]}

metals = list(densities.keys())
densities_pairs = sorted(densities.items(), key = lambda kv : kv[1][0])
#for metal in metals:
#    print(metal, densities[metal])

#FILTERING OUT: PRINTS ONLY IF INDEX POSITION 0 OF VALUES IN DENSITIES DICTIONARY ARE OVER 10
for k, v in sorted(densities.items(), key = lambda kv : kv[1][1], reverse = True):
    if v[0] > 10:        
        print(k,v)

#for metal in metals:
#    print(’{0:>8} = {1:5.1f}’.format(metal,densities[metal]))

values = [1, 3, 5]

#INCREMENTAL SUM/ADDING OF ALL NUMBERS IN LIST WITH FOR LOOP
total_val = 0

for val in values:
    total_val += val
print('TOTAL: ' + str(total_count))
    
#ANOTHER WAY TO ADD UP ALL NUMBERS IN LIST
def sum_values(l):
    sumV = 0
    for val in l:
        sumV += val
    return sumV
print(sum_values(values))

#LOOPING TO CALCULATE NEW SET OF VALS FROM LIST AND APPENDING TO NEW LIST 
#(here the new list is converted from GBP vals to CNY)
british_sterling = [1,2,5,10,20]
chinese_yuan = []
for num in range(len(british_sterling)):
    chinese_yuan.append(british_sterling[num] * 7)

print(british_sterling)
print(chinese_yuan)

#LOOPING WITH INDEX VALS
#LOOP RANGE: uses the index to loop, what follows must correspond (compare below)
replace_me = [1,6,4,90]
for val in range(len(replace_me)):
    replace_me[val] = replace_me[val] * 2
print(replace_me)

#LOOP VALUE: each value is looped through (compare above)
replace_me = [1,6,4,90]
index_count = 0
for val in replace_me:
    replace_me[index_count] = replace_me[index_count] * 2
    index_count += 1
print(replace_me)

#LOOPING WITH RANGE
#start(index),stop(inclusive),step. below starts at 4, so prints 4, then 180
some_nums = [1,6,4,90, 180,222]
for val in range(2,5,2):
    print(some_nums[val])

#USING BREAKS: looking for the letter 'h'
my_word = 'xylophone'
for letter in my_word:
    if letter == 'h':
        print('Got it! It is',letter)
        break
    else:
        print('It is not', letter)






nums = [1,5,30,200,101,100,22]
print("length",len(nums))
print(list(range(len(nums))))
for index in range(len(nums)):
    if nums[index] > 100:
        print("break:", nums[index], "with index", index)
        break
    
nums = [1,5,30,200,101,100,22]
for index in range(len(nums)):
    print("loop index", index, "with value", nums[index])
    if nums[index] > 100:
        print("break:", nums[index], "with index", index)
        break
print("**************")
nums = [1,5,30,200,101,100,22]
for index in range(len(nums)):
    print("loop index", index, "with value", nums[index])
    if nums[index] > 100:
        print("need to break:", nums[index], "with index", index)
    else:
        print("Oh, you forgot to break the loop", nums[index], "with index", index)
        

colours = ["red", "green", "red", "green", "blue", "green", "green"]
d = {}
for item in colours:
    
    if item not in d:
        d[item] = 1
        print(d, "first time")
        
    else: 
        d[item] = d[item] + 1
        print(d)

#######################################


#LOOP WITH BREAK


#CREATING A NESTED LOOPS. THIS FOR LOOP CREATES A DICT BUT REPLACES EACH VALUE

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
    
# CREATES DICT OF KEY AND VALUE PAIR USING ZIP()
# List of strings
listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
    
# List of ints
listOfInt = [56, 23, 43, 97, 43, 102]

# Create a zip object from two lists
zipObj = zip(listOfStr, listOfInt)

# Create a dictionary from zip object
dictOfWords = dict(zipObj)

# Create a zip object from two lists
zipObj = zip(listOfStr, listOfInt)
 
# Create a dictionary from zip object
dictOfWords = dict(zipObj)

print(dictOfWords)

# MULTIPLICATION TABLE

for i in range(1,11):
    for j in range(1,11):
        print('{0:>3}'.format(i * j), end='')
    print('\n')




