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

#The first button is for you to start running your code until the break point .
#The second button allows you to run your code line-by-line until the breakpoint.
#The third one is for stepping into the sections (class and functions) that you would
#like to dig into more and the fourth button is for you to step out when you feel that
#the error is not related to the current section .
#The fourth button is for you to go to the next breakpoint (if you have setup
#multiple ones).
#The last, square shaped button is for you to exit debugging mode and go back to
#normal coding mode .
