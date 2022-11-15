#write a function that given as input a number
#representing degrees in celsius
#returns the corresponding degrees in fahrenheit

def celcius_fahrenheit(degrees):
    degrees_fahrenheit_celcius = degrees * (9/5) + 32
    return degrees_fahrenheit_celcius 
print(type(celcius_fahrenheit(100)))