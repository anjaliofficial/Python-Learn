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

tup2 = ("geeks ", "for")
print("\nTuple with the use of string", tup2)

#Note  - The creation of a Python tuple without the use of parentheses is known as Tuple Packing. 

#Access tuple items 

tup3 = tuple([1,2,3,4,5])

#Access tuple items 
print(tup3[0])
print(tup3[-1])
print(tup3[-3])



#Boolean Data types in python

print(type(True))
print(type(False))
# print(type(true))


#Set Data types in pYTHON 

#Initializing empty set 
s1 = set()

s1 = set("Geeks for geeks")
print("Set with the use of the list ", s1)

s2 = set("Geeks for geeks")
print("Set with the use of the list ", s2)


#Set is unorderd 



#Access set items

# set items cannot be accessed by referring to an index, since sets are unorderd the items have no index 

set1 = set(["Geeks", "For", "Geeks"])
print(set1)


#But we can loop through the set items using for loop, or ask if a specified values is present in a set, by using the in the keyword
# 
# #Loop through set 

for i in set1: 
    print(i, end = " ")

#Check if items exist in set 
print("Geeks" in set1)


#Dictionary Data types 


#Creating a dict in python 

#Initialize empty dict 
d = {}

d = {1: 'Geeks', 2: "for", 3: "geeks"}
print(d)


#Creating dict using dict( ) constructor 
d1 = dict({1: 'Geeks', 2: 'For', 3: "Geeks"})
print(d1)


#Accessing  key - values in dict 

#In order to access the items of a dict refer to its key name. key can be used inside square brackets. Using get() method we can access the dict elements 

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(d['name'])

#Accessing a element using get 
print(d.get(3))


#-------------------------------------------------------------------------------------

# Python data types exercise questions 
# Q1. Code to implement basic list operations




fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("grape")
print(fruits)
fruits.remove("orange")
print(fruits)



#Q2. Q2. Code to implement basic tuple operation

coordinates = (3, 6, 5,4)
print(coordinates)
print("X-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])



