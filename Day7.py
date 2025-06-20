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


#    Issues with the Initial Approach
# Lengthiness: Writing separate loops for each number from 1 to 10 makes the code lengthy.
# Inflexibility: If you need to print tables from 1 to n instead of 1 to 10, you would have to write n loops, which is impractical.

#SOO Thats why we use nested loop

for i in range(1, 6):
    for j in range(i, i*10+1, i):
        print(j, end=" ")
    print()




#Nested loop 

for i in range(1, 3):
   j = 1
   while  j < 3: 
      print(i, j)
      j = j+1
      print("Anjali")


#Applications : Traversing a list of lists 

ll = [[10, 20, 30 ], [40, 50, 60], [70, 80]]
for l in ll:
   for x in l:
      print(x, end = " ")
print()
   