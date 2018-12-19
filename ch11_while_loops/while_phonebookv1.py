def inputDict(phoneBook_dict):
    keysNo = len(phoneBook_dict.keys())
    while True:
        print('Type "exit" to quit phonebook')
        inputKey = input('Enter your name: ')

        if inputKey in phoneBook_dict:
            print('Sorry, that already exists, please try again.')
            inputDict(phoneBook_dict)
            return 'sorry exit', keysNo
        elif inputKey == 'exit':
            break
        else:
            inputPhone = input('Enter the last 3 digits of your phone number: ')
            inputLuckyNo = input('Enter your lucky number: ')
            inputPostCode = input('Enter your post code: ')
            inputTownCity = input('Enter your town/city: ')
            inputBirthYear = input('Enter your year of birth: ')
            queenAge = queensAge(inputBirthYear)
            phoneBook_dict[inputKey] = inputPhone, inputLuckyNo, inputTownCity, inputPostCode, inputBirthYear, queenAge
            print('\nThanks for your entry', inputKey)
            
            sortMethod(phoneBook_dict, keysNo)
            return phoneBook_dict, keysNo
        
def sortMethod(phoneBook_dict, keysNo):
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
        print('\nNext person please')
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
