#Day 6 of learning python 


#Break  in python 

# Loops in Python can be controlled using jump statements like break. These statements allow you to change the flow of execution by exiting loops prematurely or skipping iterations.

# The break statement specifically is used to terminate the loop when a certain condition is met, allowing the program to continue executing the code that follows the loop.

n = 15
for x in range(2, n+1):
    if n % x == 0:
        print(x)
        break
    

#Using while loop with break statement 


n = 15
x = 2
while x <=n:
    if n % x == 0:
     print(x)
    break
x = x + 1


#Exercise : predict output 
i = 1
while i<=5:
   if i == 3:
      break
   print(i)
   i = i+1
   print(i)



#--------------------------------------------------------------------------------

#Continue in python 
# Lo/ops in python can be controlled using jump statement like continue. 
# 

# l = [10, 16, 17, 18, 19, 15]
# for x in l:
#    if x % 5 == 0:
#       continue
#    print(x)


#   Alternative solutions without continue
l = [10, 16, 17, 18, 19, 15]

for x in l:
    if x % 5 != 0:
        print(x)



#When to use continue

# continue is always optional and can often be replaced with conditional statements. However, it makes the code more elegant, especially when dealing with long loops that contain multiple operations.


#Example with while loop 

# i = 0 
# while i<=5:
#    if i == 3:
#       i = i+1
#       continue
#    print(i, i*i)
#    i = i+1



# Last exercise 
l = [10, 16, 17, 18, 9, 15, 21, 13]

for x in l :
   if x % 5 == 0:
      continue
   if x %7 == 0:
      break
   print(x)
print("Bye")



#-----------------------------------------------------------------------------------

#Nested Loops in python 
# Initial Approach: Separate Loops for Each Number


for i in range (1, 11, 1):
   print(i, end = " ")
   print() 

   
for i in range (2, 21, 2):
   print(i, end = " ")
   print() 
   

   
for i in range (3, 31, 3):
   print(i, end = " ")
   print() 