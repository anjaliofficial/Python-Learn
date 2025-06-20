#Day 6 of learning python 


#WWhile looops in Python 

#Hoe the conditions work 
# The condition_test is a Boolean expression that determines whether the loop continues to execute. As long as this condition remains true, the statements inside the loop will keep running. Once the condition becomes false, the loop will terminate,
# and the program will move on to the next set of instructions outside the loop.


i = 0
while i <5:
    print("Anjali")
    i = i+1



#Understandiong the counter variable 

# In this example, i is a counter variable initialized to 0.
# The while loop checks if i is less than 5 (i < 5). 
# If the condition is true, it prints "GeeksforGeeks" and increments i by 1. 
# This process repeats until i is no longer less than 5, resulting in the message being printed five times.

#Changing initial values 
i = 1 
while i <5: 
    print("Anjali")
    i = i+1



#Infinite loops 
# If you create a while loop where the conditiion never becomes false, the loop will run idenfinitely. 
# for example:
# i = 0 
# while i <5: 
#     print("Anjali")
    


# Applications of infinite loops 
# Infinite loops have practical applications in real-world scenarios. For instance,
# web servers like Apache use infinite loops to continuously listen for incoming requests.
#  By setting the condition to True,\
# you can create loops that run indefinitely until an external condition breaks them

# while True :
#     print("Anjali")


#final Example : User input controlled while loop 

n = int (input("Enter a number: "))
i = 0 
while i <n :
    print("Softwaricaaa")
    i = i +1


#----------------------------------------------------------------------------------------------------------------
#range() in python 

# the range () function python is used to generate a sequenc eof numbers ,.
#it is used in for loops () to iterate over a sequence of numbers, s
# allowing you to execute a block of code multiple times.



#Forms of the range ( )fun
# range(stop): Generates numbers from 0 up to stop minus 1.
# range(start, stop): Generates numbers from start up to stop minus 1.
# range(start, stop, step): Generates numbers from start up to stop minus 1, incrementing by step.



#Range (stop)

# When you call range() with a single argument, it generates numbers starting from 0 up to,
#  but not including, the specified stop value./


for i in range(6):
    print(i, end = " ")
print()


#   range (start, stop)
# By providing two arguments to range(), 
# you can specify the starting point of the sequence as well as where it should end.


#Example: 

for i in range(5, 30):
    print(i, end = " ")
print()




#range(start, stop, step)
# With three arguments, range() allows you to define the increment between each number in the sequence. 
# The step can be positive or negative, determining whether the sequence increments or decrements.

#Example
for i in range (0, 10, 2):
    print(i, end = " ")
    print()




#Additional examples and exercise 


#Example 1:  Range with negative step 

# When the step is negative, the sequence will decrement.

for i in range (20, 0, -2):
    print(i, end = " ")
print()


#Ex2 : Range withh negative step and different parameters 

for i in range(20,0, -3):
    print(i, end = " " )
print()







#-------------------------------------------------------------------------------------------------------------


#For Loop In python 

# The for loop in Python is used to iterate through a sequence.
#  A sequence can be a list, tuple, string, set, or a range of numbers. 
# The for loop allows you to execute a block of code for each item in the sequence.


# Iterating Through Different Iterables
# You can use the for loop to iterate through various types of iterables in Python:

# List: A collection of items that can be of any type.
# Tuple: An immutable sequence of items.
# String: A sequence of characters.
# Set: A collection of distinct items.
# Range: A sequence of numbers.


# 1. Iterate through a list

# Iterate through a list and print each item

l = [10, 20, 30, 40]
for x in l:
    print(x)


#2. Iteraung through a String 

# A string is a sequence of characters
#Iterate through a string a print each character
s = "Anjali"
for x in s:
    print(x)
    
# 3. Iterating Through a Range

# The range function generates a sequence of numbers,
# which can be iterated over using a for loop. 

# Iterate through a range of numbers and print each
for x in range(5):
    print(x)


#Using for loop with range and if statement
# You can combine the for loop with conditional statements to perform actions based on certain conditions
# Print multiples of 6 within a range
for x in range(20):
    if x % 6 == 0:
        print(x)



#Iterating with index using range(len())
# Sometimes, you may need to know the index of each item while iterating through a list. 
# You can achieve this by using the range() function along with the len() function:

l = [10, 20, 30, 40]
for i in range (len(l)):
    print(l[i])


# However, this method is not recommended when you can directly iterate through the list.
# It's more efficient and simpler to use:

l = [10, 20, 30 ,40 ]
for x in l:
    print(x)



#Iterating with index and element 
# if you need both the index and the element while iterating, you can modify the loop as follows:

# Iterate through a list and print index and element
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(i, l[i])