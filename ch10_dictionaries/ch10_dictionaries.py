#CREATING A DICTIONARY
mob = {'amanda': 858, 'loren': 264, 'ottilie': 344, 'mabel': 914}

#UPDATING DICTIONARY ENTRIES
mob['mabel'] = '3914'
mob['amanda'] = 8585
mob['ottilie'] = 8344
mob['loren'] = 8264

print(mob)

del mob['mabel']

print(mob)

print(list(mob.values()))

#CHECKING IF A KEY IS IN DICT, IF NOT ADDING IT - AVOIDING KEY ERRORS

k = 'chen'

if k in mob:
    print(k + ':', mob[k])  
else:
    print('Not found')
    mob['chen'] = 1234

print(mob)

#SORTING USING LAMBDA

counts = {'a':3, 'c':1, 'b':5}
#creating a new var to compile all keys in list
labels = list(counts.keys())
#sorting the labels using lambda
labels.sort(key=lambda i:counts[i])

toppings = {
    '1':['Pepperoni', 110],
    '2':['Pineapple', 50],
    '3':['Extra Cheese', 140],
    '4':['Olives', 55]
}

options = list(toppings.keys())

#sort by alphabetical topping 
options.sort(key=lambda i:toppings[i])
#sort by calories
options.sort(key=lambda i:toppings[i][1])
print(options)
#inverse sort by calories
options.sort(reverse=True, key = lambda i: toppings[i][1])
print(options)


#=================================================================
#MORE SORTING OF DICTIONARIES
#=================================================================


densities = {'iron': [7.8, 14, 76], 'gold': [19.3, 364, 15], 'zinc': [7.13, 7, 7], 'lead': [11.4, 6, 83]}

metals = list(densities.keys())
print(metals)
print(metals)
#Sorts by key, displays both kv
metals.sort(reverse=True, key=lambda k:densities[k])
print(metals)

bySharePrice = list(densities.items())
sorted(densities.items(), key = lambda kv : kv[1])
print(bySharePrice)

#REVERSE SORTS MY METALS LIST BY THE THIRD VALUE, 3RD VALUE = FREQUENCY OF EACH EXPERIMENT
metals = list(densities.items())

metals2 = sorted(densities.items(), key = lambda kv : kv[1][2], reverse = True)
print(metals2)

#REVERSE SORT() MY METALS LIST BY THE SECOND VALUE (COMPANY SHARE PRICE)

metals3 = list(densities.items())

metals4 = sorted(densities.items(), key = lambda kv : kv[1][1])
print(metals4)

#USES .SORT FUNCTION TO DO THE ABOVE
metals5 = list(densities.items())
metals5.sort(key = lambda kv : kv[1][1])
print(metals5)

#USES .SORT FUNCTION - NOTE THE NEED TO REFERENCE THE DICTIONARY IN LAMBDA
# TO SORT BY VALUES
metals6 = list(densities.keys())
metals6.sort(key = lambda k : densities[k][1])
print(metals6)

#=================================================================
#PHONEBOOK EXERCISE 
#=================================================================

def inputDict(phoneBook_dict):
    keysNo = len(phoneBook_dict.keys())
    if keysNo < 5:
        inputKey = input('Enter your name: ')
#        NEED TO TEST THIS
        if inputKey in phoneBook_dict:
            print('Sorry, that already exists, please try again.')
            inputDict(phoneBook_dict)
            return 'sorry exit', keysNo
        else:
            inputPhone = input('Enter the last 3 digits of your phone number: ')
            inputLuckyNo = input('Enter your lucky number: ')
            inputPostCode = input('Enter your post code: ')
            inputTownCity = input('Enter your town/city: ')
            inputBirthYear = input('Enter your year of birth: ')
            queenAge = queensAge(inputBirthYear)
            phoneBook_dict[inputKey] = inputPhone, inputLuckyNo, inputTownCity, inputPostCode, inputBirthYear, queenAge
            print('Thanks for your entry', inputKey)
            print(keysNo)
            print(phoneBook_dict)
            
            sortMethod(phoneBook_dict, keysNo)
            return phoneBook_dict, keysNo

    else:        
        print('Our records are full I\'m afraid, please come back next time!')
     
def sortMethod(phoneBook_dict, keysNo):
    print(keysNo)
    if keysNo > 1:
        sortType = input('Do you want to sort by (1) Name, (2) Town/city, (3) Lucky number? (1/2/3) ')
        if sortType == '1':
            print(sorted(phoneBook_dict))
        elif sortType == '2':  
            townList = sorted(phoneBook_dict.items(), key = lambda v : v [1][3])
            print(townList)
        elif sortType == '3':
            luckyNoList = sorted(phoneBook_dict.items(), key = lambda v : v [1][1])
            print(luckyNoList)          

    else:
        print('Next person please')
        inputDict(phoneBook_dict)

def queensAge(inputBirthYear):
    queenAge =  int(inputBirthYear) - 1926 
    return queenAge

phoneBook_dict = {}
keysNo = len(phoneBook_dict.keys())
phoneBook_dict = inputDict(phoneBook_dict)

f = open('phonebook.txt', 'w+')
f.write(str(phoneBook_dict))
f.close()



