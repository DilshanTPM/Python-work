# String data type [First Type]

# literal assigment
first = "Dave"
last = "Gray"

# use ctrl and / to uncomment sections !!!!

# print (type(first))
# print (type(first) == str)
# print (isinstance(first, str))  

# # Constructor Function
# # pizza  = str("Pepperoni")
# # print (type(pizza))
# # print (type(pizza) == str)
# # print (isinstance(pizza, str))

#Concatenation [Adding 2 strings together to form a larger string]
fullname = first + " " + last # "" - adds a space between the first and last name
print (fullname)

fullname += "!"
print (fullname)

# Casting a number to a string [Changing a number to a string]
decade  =str(1980)
print (type(decade))
print(decade)

statement = "I like to lift the heavy weights of  " + decade + "s."
print (statement)

# Multiple lines # Long statement 
multiline = '''
Hey, how are you?

I was just checking in.

                           All good?

.....
'''
print(multiline)


# Escaping special characters

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'  #\t = tab, \n = new line , use a \ to use special characters

print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline)) #checks original length of the 'multiline' counts every character
multiline += "                                               "
mutiline = "                        " + multiline
print(len(multiline))

print(len(multiline.strip())) # Clears the white space
print(len(multiline.lstrip())) # clears the white space on the left
print(len(multiline.rstrip())) # clears the white space on the right

print("")

# Build a menu
title = "menu".upper() 
print(title.center(20,"="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Tea".ljust(16, ".") + "$3".rjust(4))
print("Biscuits".ljust(16, ".") + "$9".rjust(4))

print("")

# String index values
print(first[0]) # prints the first charachter 
print(first[-1]) #prints the last charachter of any string of any length
print(first[1:-1])
print(first[1:])
print(first[0:-1])

# Some mentods to return Boolean data [ Boolean data = true or false data]
print(first.startswith("D"))
print(first.endswith("z"))


# Boolean data type
myvalue = True
X = bool(False)
print(type(X))
print(isinstance(myvalue, bool))

#Numeric data types

print("")

# Interger type

price = 100
best_price = int(80)
print(type(best_price))
print(isinstance(best_price, int))

# Float type
gpa =3.45
y = float(1.14) # constructor
print(type(gpa))

print("")

# Complex type

comp_value = 5+3j
print(type(comp_value))
print(comp_value.imag)
print(comp_value.real)

print("")

# Buil-in functions for numbers

print(abs(gpa)) # abs = absoulte value
print(abs(gpa * -1))

print(round(gpa)) # rounds to the interger


print(round(gpa, 1)) # rounds to the decimal place speciifed 

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


#casting a string to a number
zipcode = "1001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data 
zip_value = int("New York")