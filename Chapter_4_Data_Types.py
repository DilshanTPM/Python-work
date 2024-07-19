# String data type

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

#Concatenation 
fullname = first + " " + last
print (fullname)

fullname += "!"
print (fullname)

# Casting a number to a string
decade  =str(1980)
print (type(decade))
print(decade)

statement = "I like to lift the heavy weights of  " + decade + "s."
print (statement)