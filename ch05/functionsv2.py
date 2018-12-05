#PRACTISING SUPERCLASS AND SUBCLASS THROUGH AN AGEIST STEREOTYPES GAME
class human():
#   def __init__(self):
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
    def __init__(self, name, toy):
        self.toy = toy        
    def talkgibberish(self):
        print('gurgle gurgle gurgle, you\'re just a baby! Here is your {}'.format(self.toy))

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

if int(age) <=13:
    toy = input('Toy: ')
    baby = child(name, toy)
    baby.talkgibberish()
    
elif int(age) >=14 and int(age) <=21:
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
  
