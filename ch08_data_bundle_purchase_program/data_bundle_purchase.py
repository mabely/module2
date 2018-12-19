# -*- coding: utf-8 -*-

def DataBundlePurchase(truepin, balance):
    if checkpin(truepin):
        print('Welcome to BT.')    
        actions = input('Would you like to:\n1 Check balance\n2 Purchase data bundle\nEnter 1/2: ')
#        print(actions)

        if actions == '1':
            print('else')
            return('Your credit balance is £{}'.format(balance))
            
        elif actions == '2' and checkmobile():
            databundle(balance)
            
    else:
        print('Your account has been locked, please contact us at 020 123 456.')
        return('accountlocked')


#BUYING DATA BUNDLE
#def databundle(balance):
#gb1 = 5
#gb5 = 10
#gb10 = 20

    print('Our data bundles are as follows: \n1. 1GB --- £5 \n2. 5GB --- £10 \n3. 10GB --- £20 \nYour current balance is £{}'.format(balance))
    
    if balance < 5:
        print('Sorry you have insufficient funds, please top up.')
    elif balance >=5 and balance <10:
        print('Buy A')
    
    elif balance >=10 and balance <20: 
        print('Buy A or B')
    elif balance >=20:
        print('Buy anything!')        
    
#CHECKING MOBILE NUMBER
def checkmobile():
    mobnumber1 = input('Please enter your phone number: ')
    mobnumber2 = input ('Please enter your phone number again: ')
    if mobnumber1 == mobnumber2:
        return True
    else:
        return False

#PIN CHECKING FUNCTIONS
def checkpin(truepin):
    if checkpin_prompt(truepin):
        return True
    print('\nPlease try again (second attempt)')
    if checkpin_prompt(truepin):
        return True
    print('\nPlease try again (final attempt)')
    if checkpin_prompt(truepin):
        return True
    return False

def checkpin_prompt(truepin):
    attempt = input('Please enter your pin: ')
    if attempt == truepin:
        return True
    else:
        print('\nPin incorrect')
        return False   
    
#actions = {
#    1: ["Check balance", balance],
#    2: ["Purchase data bundle", ]
#        }
        
    