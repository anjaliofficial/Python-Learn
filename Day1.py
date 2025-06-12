# Simple greeting
print("Hello, World!")

# Asking user for their name
name = input("Enter your name: ")
print("Hello,", name, "Welcome!")

# Single variable assignment
s = "Bob"
print(s)

# Multiple variables
S = "Alice"
age = 25
city = "Kathmandu"
print(S, age, city)

# Taking two inputs at once
x, y = input("Enter two values (e.g., boys girls): ").split()
print("Number of boys:", x)
print("Number of girls:", y)

# Taking three inputs at once
x, y, z = input("Enter three values (e.g., total boys girls): ").split()
print("Total number of students:", x)
print("Number of boys is:", y)
print("Number of girls is:", z)

#Take  conditional input from user in python 

age_input = input(" Enter your age ")
age = int (age_input)

if age <0:
    print("Please Enter a valid age ")
elif age<18:
    print( " Ypur are a minor ")
elif age >= 18 and age<65:
    print("You are an adult")
else: 
    print("you are a senior citizen")