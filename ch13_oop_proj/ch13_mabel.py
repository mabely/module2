# -*- coding: utf-8 -*-

#====INIT, METHODS====#

class Person:
    # The init method establishes the attributes of the class
    def __init__(self,name,age,gender,color):
        # self refers to the attribute of that particular instance
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not recognised!')
        self.color = color
        
    def greetingInformal(self):
        print('Hey', self.name)
        
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr', self.name)
        else:
            print('Welcome, Ms', self.name)
            
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome, young', self.name)
        elif self.age > 60:
            print('Welcome, venerable', self.name)
        else:
            self.greetingFormal()
    
#Creating an instance with above details
person1 = Person('Emily',38,'f','red')
person2 = Person('Carl',23,'m','purple')
person2.name 
person2.color      
person2.greetingFormal
person2.greetingAgeBased

#====SUBCLASSES====#    

class Wizard(Person):
    # Explicitly invoking superclass init but adding spell and house as well
    def __init__(self,name,age,gender,color,spell,house):
        # This is how to invoke the stuff you want from superclass init
        Person.__init__(self,name,age,gender,color)
        self.spell = spell
        self.house = house
        
    # Overwriting the greetingFormal in Person class by redefining method
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr', self.name, end=' ')
        else:
            print('Welcome, Ms', self.name, end=' ')

        print('- to the Hogwarts School of Witchcraft and Wizardry!')
        
    def greetingHouse(self):
        if self.house == 'Gryffindor':
            print('What a fine house Gryffindor is, for where dwell the brave at heart, their daring, nerve and chivalry set Gryffindors apart. Welcome Gryffindor!')
        elif self.house == 'Hufflepuff':
            print('Hufflepuffs are always welcome here, for they are just and loyal. Those patient Hufflepuffs are true, and unafraid of toil, as the Sorting Hat says.')
        elif self.house == 'Ravenclaw':
            print('Ah a Ravenclaw, the house where the cleverest witches and wizards live. You shall find a great home here.')
        elif self.house == 'Slytherin':
            print('An ambitious and loyal Slytherin! You could be the next Merlin, for he was a Slytherin too!')
     
    # Here I initially made the mistake of naming the method 'spell' (same as Wizard attribute), which threw a TypeError that a string obj is not callable.
    # Note to self to avoid naming cross-overs between attributes and methods
    def doSpell(self):
        print(self.spell + '!')

person3 = Wizard('Dumbledore',88,'m','silver','Disapparate','Gryffindor')
person4 = Wizard('Harry Potter',29,'m','Gold','Expecto Patronum','Gryffindor')
person5 = Wizard('Bellatrix Lestrange',47,'f','green','Imperius','Slytherin')
person6 = Wizard('Newt Scamander',122,'m','blue','Appare Vestigium','Hufflepuff')
# The following calls the redefined method for Wizards
person4.greetingFormal()
# Note that rest of methods of original superclass Person are inherited
person4.greetingInformal()
person4.greetingHouse()
person4.doSpell()
