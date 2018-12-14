densities = {'iron': [7.8, 14, 76], 'gold': [19.3, 364, 15], 'zinc': [7.13, 7, 7], 'lead': [11.4, 6, 83]}

#metals = list(densities.keys())
#print(metals)
#print(metals)
#Sorts by key, displays both kv
#metals.sort(reverse=True, key=lambda k:densities[k])
#print(metals)

#bySharePrice = list(densities.items())
#sorted(densities.items(), key = lambda kv : kv[1])
#print(bySharePrice)

#REVERSE SORTS MY METALS LIST BY THE THIRD VALUE, 3RD VALUE = FREQUENCY OF EACH EXPERIMENT
metals = list(densities.items())

metals2 = sorted(densities.items(), key = lambda kv : kv[1][2], reverse = True)
print(metals2)

#REVERSE SORT() MY METALS LIST BY THE SECOND VALUE (COMPANY SHARE PRICE)

metals3 = list(densities.items())

metals4 = sorted(densities.items(), key = lambda kv : kv[1][1])
print(metals4)

#USES .SORT FUNCTION TO DO THE ABOVE
metals5 = list(densities.items())
metals5.sort(key = lambda kv : kv[1][1])
print(metals5)

#USES .SORT FUNCTION - NOTE THE NEED TO REFERENCE THE DICTIONARY IN LAMBDA
# TO SORT BY VALUES
metals6 = list(densities.keys())
metals6.sort(key = lambda k : densities[k][1])
print(metals6)


