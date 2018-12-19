# -*- coding: utf-8 -*-

#USE OF PRINT STATEMENTS HELPS TO DEBUG CODE. THE BELOW SHOWS THAT INPUT RETURNS
#STRING, WHICH WOULD THROW AN ERROR UNLESS THE USERINPUT WAS CAST INTO AN INT

userInput = input('Please give a number ')
#    result = userInput - 2
print(type(userInput))


#USE OF THE DEBUGGING SYSTEM ALLOWS PLACING OF BREAKPOINTS AND WHEN RUN, IT 
#SHOWS THE PROCESS THE CODE IS RUN


userInput = input('please give a number ')

def simpleOperation(userInput):
    intInput = userInput
    result = int(intInput) - 2
    return result

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)