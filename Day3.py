
# Python Keywords


#getting list of all python keywords 

import keyword
# Printing all keywords at once using "Kwlist()"
print("The list of keyword is : ")
print(keyword.kwlist)

#Category and keywords in python 

# Values keywords --- True, false , None 
#operator keyword s- and, or, not, in, is
# Control Flow Keywords	---------if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert
# Function and Class	----------def, return, lambda, yield, class
# Context Management	-----------------with, as
# Import and Module	-------------import, from, as
#  Scope and Namespace-------------------	global, nonlocal
# Async Programming----------------	async, await


#Value Keywords: True, False, None Keyword, del
print(False == 0)
print(True == 1)

#print(False == 0)
print(True == 1)

# True + True + True is  3
print(True + True + True)

# True + False + False is  1
print(True + False + False)

# None isn't equal to  0  or an empty list []
print(None == 0)
print(None == [])


#Operator Keywords : And, or, not, in,is

# and Keyword - return 'True' if both the operands are 'True'
# or Keyword - return 'True' if at least one operand is 'True'
# not keyword - returns 'True' if the expression is 'False', and vice versa.

a = True
b = False

# Logical operations
print(a and b)  # AND: True if both a and b are True
print(a or b)   # OR: True if at least one of a or b is True
print(not a)    # NOT: Inverts the value of a

# iN Keywords (Membership Operator )-------Checking a vlaues exists in a sewuance like a list, tuple, string. 
# It returns Trure is values is found 

# example 1
print(3 in [1,2,3])

# example 2
if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")

# is keyword - Check if two variables point to the same object in memory. It returns True if the objects are identical
# 
# example 1.

print(2, is 2)
example 2[1,2,3]
b = a
c = [1,2,3]

 #True a and b refer to the samme object 

Print(a, b)

# True: a and b refer to the same object
print(a is b)  

# False: a and c have same value but are different o
