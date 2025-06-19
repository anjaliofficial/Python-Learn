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




#Converting Containers List 

t = (10, 20, 30 )
print(list(t))

s = {10, 20, 30}
print(list(s))


# Here, a tuple and a set are both converted to lists. Note that while tuples maintain order, sets do not.
#  However, once converted to a list, the order is preserved in the list.


#Binary, octual ,And Hexadecimal Conversion s

#Python allows ypu to convert intergers to thier binary, octal, and hex representions using the bin(), oct(), and hex() function, respectively 

a = 20
print(bin(a))
print(hex(a))
print(oct(a))


#Convert back to decimal 
a = "1001"
print(int(a, 2))    # Output: 9
b = "12"
print(int(b, 8))    # Output: 10
c = "A1"
print(int(c, 16))   # Output: 161


#----------------------------------------------------------------------------------------------------------------------------

#if , else, and elif in python 

#if
#else
#Nested-if
#if-elif-statements. 



#If satatement 
# If the simple code of block is to be performed if the condition holds true then if statement is used. 
# Here the condition mentioned holds true then the code of the block runs otherwise not.


#Example: 
if 10 > 5: 
    print("10 Greater than 5")

print("Program ended")


#If else Statement 
#In conditional if Statement the additional block of code is merged as
#  else statement which is performed when if condition is false. 


x = 3
if x == 4:
    print("Yes")
else: 
    print("No")



#Example 2: Example 2: You can also chain if..else statement with more than one condition. 

# if..else chain statement
letter = "A"
 
if letter == "B":
  print("letter is B")
   
else:
     
  if letter == "C":
    print("letter is C")
     
  else:
       
    if letter == "A":
      print("letter is A")
       
    else:
      print("letter isn't A, B and C")



#Nested If statement 
#If statement can also be checked inside other if statement. 

# Nested if statement example
num = 10
 
if num > 5:
   print("Bigger than 5")
 
   if num <= 15:
      print("Between 5 and 15")


#if - elif Statement 

# The if-elif statement is shortcut of if..else chain. While using if-elif statement at the end 
# else block is added which is performed if none of the above if-elif statement is true.

# if-elif statement example
 
letter = "A"
 
if letter == "B":
   print("letter is B")
 
elif letter == "C":
   print("letter is C")
 
elif letter == "A":
   print("letter is A")
 
else:
   print("letter isn't A, B or C")