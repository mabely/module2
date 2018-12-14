

#PRACTISING SUPERCLASS AND SUBCLASS THROUGH AN AGEIST STEREOTYPES GAME
class human():
#   def __init__(self):
# When initiating, it stores the attributes of that class into memory space 

    def __init__(self, name):
        self.name = name        
    def eat(self):
        print('nom')
    def greeting(self):
        print('Hi {}!'.format(self.name))
    def laugh(self):
        print('hahahaha!')        
    def cry(self):
        print('sob sob sob, I\'m so sad')
        
class child(human):
# Self is always required in method defs and init to refer to itself
# In memory, it makes sure it is unambiguous to which class/subclass 
# those attributes/functions belong - eg. below for function talkgibberish,
# self makes sure that the child class is initialised with the name (from 
# parent/human class) and toy (new var to this class, gathered from user 
# input below). 
    def __init__(self, name, toy):
        self.toy = toy        
    def talkgibberish(self):
        print('Here is your {}'.format(self.toy))

class adult(human):
    def adultgreeting(self):
        #print('Hello there!')
        print('Hello {}!'.format(name))
    
    def joke(self):
        print('Want to hear a joke? Of course you do! What do you call cheese that isn\'t yours? Nacho Cheese.')

class millennial(adult):
    def socmedia(self):
        print('Omg I just saw your Instagram profile...')
    
    def talknonsense(self):
        print('Looks like you\'re a millennial, let\'s take a selfie!')
    
age = input('Please enter your age: ')
name = input('Please enter your name: ')
jonny = adult('Jon')

if int(age) <=3:
#Get input from user
    toy = input('Toy: ')
#Create baby object (instance of child class), toy var and name var 
#(name from human class) are included as parameters to child class (both needed)
    baby = child(name, toy)
#All the above are needed to run the talkgibberish function for baby obj
    baby.talkgibberish()
    
elif int(age) >=4 and int(age) <=11:
    talkgibberish()
    
elif int(age) >=12 and int(age) <=21:
    genz = millennial(name)
    genz.socmedia()
    genz.eat()

elif int(age) >=22 and int(age) <=37:
    mill = millennial(name)
    mill.socmedia()
    mill.talknonsense()
    
elif int(age) >=38 and int(age) <=53:
    genx = adult(name)
    genx.adultgreeting()
    genx.joke()
    
else:
    mens = human(name)
    mens.greeting()
  
