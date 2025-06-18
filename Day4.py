#Data Types in Python 
# Numeric - int, float, complex
# Sequence Type - string, list, tuple
# Mapping Type - dict
# Boolean - bool
# Set Type - set, frozenset
# Binary Types - bytes, bytearray, memoryview

#Example of Numeric data types in python 
a = 5 # Int 
print(type(a))

b = 5.0 #Float
print(type(b))

c = 2+4j   # complex
print(type(c))


#Sequence Data Types in Python 

s = 'Welcome to the Geeks World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-2])


#List Data  types 
#Creating list in python 

#Empty list 
a = []

#List with int values 
a = [1,2,3]
print(a)

#List with mixed int and string 

b = ["Geeks", "For","Anjali", 4, 5]
print(b)

#Access List Items 

a = ["geeks", "For", "Anjali"]
print("Accessing element from the list ")

print(a[0])
print(a[2])

print("Accessing element using negative indexing ")
print(a[-1])
print(a[-3])


#Tuple Data Type s

tup1 = ()
