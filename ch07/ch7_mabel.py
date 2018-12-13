userInput = input('please give a number ')

def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)