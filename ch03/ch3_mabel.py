import datetime

now = datetime.datetime.now()
currentyear = now.year

def hello_world():
    name = input("Please type your name: ").title()
    if (name.isdigit()):
        print("Oops, please only type letters")
        hello_world()
    else:
        print("Hello {}".format(name)) 
        age_finder(name)

def age_finder(name):
    birthyear = input("Please type your year of birth: ")
    
    try:
       value = int(birthyear)
       age = str(currentyear - value)
       print("\n{} is {} years old".format(name, age))

    except ValueError:
       print("Oops, that's not a number")
       age_finder(name)

hello_world()
