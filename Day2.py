x = 5
name = "Anjali"
print(x)
print(name)



#Rules for naminf var3iables 

#valid examples 
age = 11
_colour = "lilac"
total_score = 90

# invalid example

# 1name = "Error"  # Starts with a digit
# class = 10       # 'class' is a reserved keyword
# user-name = "Doe"  # Contains a hyphen


# Assigning values to variables 
# 
#basic Assignment 

x = 5
y= 3.15
z = "Hii"



# Dynamic Typijng ""
# Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.

X = 20 
x = "Now a string"

# Assigning the same values 
# Python allows assigning the same values to multiples variables in single lone which can be usefull for initializing variables with the same values .staticmethod
a = b= c = 100
print(a, b, c)
#---------------------------------------------------------------------------

#Type Casting a variable 

# Basic Casting Functions
# int() - Converts compatible values to an integer.
# float() - Transforms values into floating-point numbers.
# str() - Converts any data type into a string.

#Example of casting 
s = "10" # initally a string 
n = int(s) #cast string to integer 
cnt = 5
f = float(cnt) # cast interger to float 
age = 25
s2 = str(age) #cast integer to string 

# display result 

print(n)
print(f)
print(s2)


# getting   the tyoe of variable 
# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

# Get and print the type of each variable
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))


#scope of variables 

#local variables
 #global variable

#local variable 
def f (): 
    a = "I am local"
    print(a)

f()
    #print (a) thi would raise an error since "local _var" is not accessible outside the function 

#global variable 
a = "I am global  "
def f():
    global a
    a = "Modified globally"
    print(a)

f()
print(a)

#delete a variable using del keyword
x = 10 
print(x)

del x 
# print(x)


# Practical examples 
#1. Swapping two varibles 
a, b = 5, 10
a, b = b, a
print(a, b)

#counting characters in a string 
word = "Anjali"
length = len(word)
print("Length of the word:", length)





# -----------------------------------------------------------
#Python Operators 

#Types of operators  in python 
# Arithmetic Operators
# Comparison Operators
# Logical Operators
# Bitwise Operators
# Assignment Operators
# Identity Operators and Membership Operators





# Example of Arithmetic Operators in Python:

# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)




#Coomparison operators in python 

a = 13
b = 33

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# logical operators in python 
# Python Logical operators perform Logical AND, 
# Logical OR and Logical NOT operations. 
# It is used to combine conditional statements.

# Exaple of logical operators in python 

a = True
b = False
print(a and b)
print(a or b)
print(not a)

#bitwise operator in python 


# Bitwise Operators in Python are as follows:

# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR

#Example of bitwise operator in python 

a = 10 
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> b)
print(a << b)


# Assignment Operators in Python


#Example of Assignment operator
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)



# Identity Operators in Python

# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

#example of identity operators in python 
a = 10
b = 20
c = a

print(a is not b)
print(a is c)



#Membership operator in python 
# In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence\

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


#------------------------------------------------

#Ternary operator in python 
#in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. 

# It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.

# Syntax :  [on_true] if [expression] else [on_false] 



#Example of ternary operator 

a, b = 10, 10 
min = a if a<b else b
print(min)  

#-----#------------------------------------------------

# Precedence and Associativity of Operators in Python

# 
# 
# This is used in an expression with more than one operator with different precedence to determine which operation to perform first.



expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")


# Operator Associativity in python 
#If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine. 
# It can either be Left to Right or from Right to Left.