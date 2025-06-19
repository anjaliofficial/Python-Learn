#Type conversion in python 

#two types of type conversion in python 
# Implicit type conversion :- this happens automatically without the programmer writing any specific code for it 
#  
#Explicit type conversion :- The  reqiures the programmar to use Specific functions or syntax to convert one type to another


#Example of Implicit type conversion 

a = 10
b = 1.5
c = a+b 
print(c) 

d = True
e = a+d
print(e)

# Here, a is an integer and b is a float. 
# When you add them, Python automatically converts
#  the integer to a float, resulting in a float value for c. Similarly, d is a Boolean, and when added to an integer,
#  it is converted to an integer (where True becomes 1), resulting in e.
    


#Explicit type conversion 

#Explicit type conversion  requires the use of function sto convert one data type to another. 
# Python provides sevral built-in function for this purpose, 
# such as  int(), float(), str(), list(), tuple(), and set().


s = "135"
i = 10 + int(s)
f = float(s)
print(i)
print(i)



#Converting between different containers 

s = "Anjali"

print(list(s))
print(tuple(s))
print(set(s))


# Converting a string to a list or tuple breaks it down into individual characters. However, 
# converting to a set removes any duplicate characters and does not preserve the order since sets are unordered collections.

#String Representation of containers 
l = ['a', 'b', 'c']
print(str(l))         	# Output: ['a', 'b', 'c']
a = 10
b = 11
print(str(a) + str(b)) 	# Output: 1011
c = 12.5
print(str(c))        	# Output: 12.5