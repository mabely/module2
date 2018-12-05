#DEMONSTRATION OF CLASS AND OBJECTS

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

#This is an object/instance of customer class
jason = Customer('Jason Taylor', 1000.0)

#DEMONSTRATION OF SUPERCLASSES AND SUB-CLASSES
class animal():
    def eat(self):
        print('yum')
        
class dog(animal):
    def bark(self):
        print('woof')
    def playtime(self):
        print('I love playtime!')    
    
class cat(animal):
    def meow(self):
        print('meow')







        