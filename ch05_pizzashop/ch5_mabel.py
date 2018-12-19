# -*- coding: utf-8 -*-

#======================================================================
#USING CLASSES TASK: CUSTOMER CLASS AND FUNCTIONS

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    Attributes:
    name: A string representing the customer's name.
    balance: A float tracking the current balance of the customer's account.
    """
    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.balance = balance
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance
    def deposit(self, amount):
        """Return the balance remaining after depositing *amount* 
            dollars."""
        self.balance += amount
        return self.balance

#OBJECT/INSTANCE OF CUSTOMER CLASS
jason = Customer('Jason Taylor', 1000.0)

#======================================================================
#CREATING SUB-CLASSES AND INHERITANCE: ROBOT SUPERCLASS AND SUBCLASSES 

class Robot():
    def move(self):
        print('...move move move...')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
class CookRobot(Robot):
    def cook(self):
        print ('I make rice')

Nana = CleanRobot()

#======================================================================
#CREATING ASSOCIATED CLASSES (COMPOSITION)

class Animal():
    def eat(self):
        print('yum')
class Dog(Animal):
    def bark(self):
        print('Woof!')
class Cat(Animal):
    def meow(self):
        print('Meow')

class Dog(Animal):
    def bark(self):
        print('Woof!')
class Robot():
    def move(self):
        print('...move move move...')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
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

