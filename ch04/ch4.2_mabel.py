def oddoreven():
    number = input('Enter a number: ')
    number = int(number)

    if (number%2==0) and (number%4==0):
        print('That\'s an even number and multiple of 4!')
    
    elif number%4==0:
        print('That\'s an even number')
        
    else:
        print('That\'s an odd number')

    return number

def oddoreven2(number):
#    oddoreven()
    check = number
    num = input('Enter another number: ')
    if int(check)%int(num)==0:
        print(str(check) + ' divides evenly into ' + str(num))
    
    else:
        print(str(check) + ' doesn\'t divide evenly into ' + str(num))

my_number = oddoreven()     
oddoreven2(my_number)

#At which point is it executing oddoreven()? 
#When I call the function, why do I need the parameters?