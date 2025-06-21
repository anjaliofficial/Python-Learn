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