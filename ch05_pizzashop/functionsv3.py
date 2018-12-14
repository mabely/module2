class Animal():
    def eat(self):
        print('yum')
class Dog(Animal):
    def bark(self):
        print('Woof!')
class Cat(Animal):
    def meow(self):
        print('Meow')
        
class Robot():
    def move(self):
        print('...move move move...')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
class CookRobot(Robot):
    def cook(self):
        print ('I make rice')

class SuperRobot():
    def __init__(self):
    #This collects all the classes relevant to this through ASSOCIATION by assigning 
    #new var/names to those classes below 
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
    def playGame(self):
        print('alphago game')
    def move(self):
        return self.o1.move()
# Returning here means you can refer to the move function that is stored
# here without needing to use the full ref of self.o1.move
    def bark(self):
        return self.o2.bark()
    def clean(self):
        return self.o3.clean()


