#penpot = {'bic': 'biro', 'highlighter': ('pink', 'yellow', 'orange')}
#
mob = {'amanda': 858, 'loren': 264, 'ottilie': 344, 'mabel': 914}

mob['mabel'] = '3914'
mob['amanda'] = 8585
mob['ottilie'] = 8344
mob['loren'] = 8264

#print(mob)
#
#del mob['mabel']
#
#print(mob)
#
#print(list(mob.values()))

#CHECKING IF A KEY IS IN DICT, IF NOT ADDING IT

#k = 'chen'
#
#if k in mob:
#    print(k + ':', mob[k])  
#else:
#    print('Not found')
#    mob['chen'] = 1234
#
#print(mob)

#SORTING USING LAMBDA

counts = {'a':3, 'c':1, 'b':5}
#creating a new var to compile all keys in list
labels = list(counts.keys())
#sorting the labels using lambda
labels.sort(key=lambda i:counts[i])

toppings = {
    '1':['Pepperoni', 110],
    '2':['Pineapple', 50],
    '3':['Extra Cheese', 140],
    '4':['Olives', 55]
}

options = list(toppings.keys())

#sort by alphabetical topping 
options.sort(key=lambda i:toppings[i])
#sort by calories
options.sort(key=lambda i:toppings[i][1])
print(options)
#inverse sort by calories
options.sort(reverse=True, key = lambda i: toppings[i][1])
print(options)




