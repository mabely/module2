def convert_distance(miles):
    km = (miles*8)/5.0
    print('Miles converted to kilometres:')
    print('Distance in miles: ', miles)
    print('Distance in kilometres:', km)
    return km

def convert_temp(centigrade):
    fahrenheit = centigrade*9.0/5.0+32
    kelvin = centigrade +273.15
#    print('Converting from centigrade to kelvin and fahrenheit')
#    print('Centigrade:', centigrade)
#    print('Fahrenheit:', fahrenheit)
#    print('Kelvin:', kelvin)
    return (str(fahrenheit)+" fahrenheit", str(kelvin)+" kelvin")

