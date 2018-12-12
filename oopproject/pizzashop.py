toppings = (
    {"name": "Pepperoni",             "calorie": 8.5},
    {"name": "Pineapple",          "calorie": 8.5},
    {"name": "Extra Cheese",            "calorie": 8.5},
    {"name": "Mushrooms",         "calorie": 8.5},
    {"name": "Jalapenos",       "calorie": 8.5},
    {"name": "Onions",    "calorie": 8.5},
    {"name": "Sweetcorn",         "calorie": 8.5},
    {"name": "Olives",       "calorie": 13.5},
    {"name": "Chicken",        "calorie": 13.5},
    {"name": "Ham", "calorie": 13.5},
)

class PizzaShop():
    def welcome():
        message="Welcome to our pizza shop"
        print(message)
    welcome()
    
class CustomerInfo(PizzaShop):
    def __init__(self, name):
        self.name=name
#        return name



class Pizza(PizzaShop):
    def createnew(self):
        print('We only serve pizza, so, an order of pizza - perfect!')
    
name = input("Enter your name: ")
customer = CustomerInfo(name)

base = input('Please choose your base:\n 1 Thin crust\n 2 Deep pan\n')
while base not in ('1','2'):
    print('Sorry, I didn\'t get that, please try again.')
    base = input('Please choose 1 or 2: ')
if base == '1':
    print('Thin crust - good choice!')
elif base == '2':
    print('Deep pan - got it')
    
    
class toppings:
    def toppingselection():
        print("please select your toppings!")
    toppingselection()

#class meat_toppings():
def pepperoni():
    pepperoni_calorie=20
    return pepperoni_calorie

def ham():
    ham_calorie=25
    return ham_calorie

def chicken():
    chicken_calorie=25
    return chicken_calorie
    
def sweetcorn():
    sweetcorn_calorie=5
    return sweetcorn_calorie
def olives():
    olives_calories=6
    return olives_calories

firstmessage=input("do you want meat on your pizza?yes/no ")
if firstmessage == "yes":
    order1=input("do you want pepperoni? yes/no ")
    order2=input("do you want ham? yes/no ")
    order3=input("do you want chicken? yes/no ")
    order4=input("Great! Now do you want veg on your pizza?")
   
    if order1 == "yes":
        pepperoni_calorie=pepperoni()
        print(order2)

    elif order1 == "no":
        print(order2)

    if order2 == "yes":
        ham_calorie=ham()
        print(order3)

    elif order2 == "no":
        print(order3)

    if order3 == "yes":
        chicken_calorie=chicken()
        print(order4)
    
    if order4=="yes":
        veg1=input("do you want sweetcorn? yes/no ")
        veg2=input("do you want olives? yes/no ")
        if veg1 == "yes":
            sweetcorn_calorie=sweetcorn()
            print(veg2)
        elif veg1=="no":
            print(veg2)
        if veg2=="yes":
            olives_calorie=olives()

else:
    if firstmessage=="no":
        veg1=input("do you want sweetcorn? yes/no ")
        veg2=input("do you want olives? yes/no ")
    if veg1 == "yes":
        sweetcorn_calorie=sweetcorn()
        print(veg2)
    elif veg1=="no":
        print(veg2)
#    if veg2=="yes":
#        olives_calorie=olives()
print("Great your pizza is in the oven!")
    
        
    
#class Base(Pizza):
#    def __init__(self, base):
        
#    def createbase(self, base):

      

#Add toppings to this class
class FinalPizza():
    #    combines both toppings, base, customer name
    def __init__(self, name):
        self.fpname = self.name
        self.fppizza = Pizza()
#        self.fpbase = Base()
#        self.fptopping = Toppings()
    
    def name(self):
        return self.fpname.name
    
    def createbase(self):
        return self.fpbase.base
    
#    Define the topping function
    
    def ordersummary(self):
        print('Thanks '+ name + '!')
        print('Your pizza will be ready shortly!')


    
newpizza = FinalPizza(name)
newpizza.ordersummary()


