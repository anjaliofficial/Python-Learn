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



