toppings = {
    '1':['Pepperoni', 110],
    '2':['Pineapple', 50],
    '4':['Olives', 55],
    '3':['Extra Cheese', 140]
}

toppings_list = list(toppings.items())

toppings2 = sorted(toppings_list, key = lambda v : v[1][0])

#print(toppings.values())

for key in toppings:
    print(key)
#     toppings.pop(key = lambda v : v[1][1])
    for value in key:
        print(value)
    