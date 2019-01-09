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

#LOOP THROUGH STRING DATATYPE
oldsentence = 'This is my sentence'
sentence = oldsentence.split()
for word in sentence:
    print(word)

#LOOPING THROUGH A STRING - RETURNS EACH CHARACTER
for words in 'Here is another sentence':
    print(words)

#LOOPING THROUGH A TUPLE/DICTIONARY
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



#######################################
#LOOP WITH INDEX VALUES


#ex10 looping with index values 
values = [3,12,9]
for index in range(len(values)):
    values[index] = values[index] ** 2
print(values)

for i in range(3,10,2):
    print(i)
      
print(list(range(3)))
print(type(range(3)))

values = [3, 12, 9, 5, 6]
for index in range(1, len(values), 2):
    print(values[index], "with index", index)
    values[index] = values[index] ** 2
    
values = [3,12,9]
for index in range(len(values)):
    print(index)
    values[index] = values[index] * 2
print(values)

#ex11 using a loop with the range function
names = ["milly", "bob", "kate", "mary", "alanis", "elly"]
for i in range(1, len(names), 3):
    print("find them", names[i])
        

#ex12 using breaks in for loops
nums = [1,5,30,200,101,100,22]
for n in nums:
    if n > 100:
        print("found", n)
        break
    
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
#LOOP WITH RANGE


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




