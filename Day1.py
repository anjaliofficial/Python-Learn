# # 
# # Simple greeting
# print("Hello, World!")

# # Asking user for their name
# name = input("Enter your name: ")
# print("Hello,", name, "Welcome!")

# # Single variable assignment
# s = "Bob"
# print(s)

# # Multiple variables
# S = "Alice"
# age = 25
# city = "Kathmandu"
# print(S, age, city)

# # Taking two inputs at once
# x, y = input("Enter two values (e.g., boys girls): ").split()
# print("Number of boys:", x)
# print("Number of girls:", y)

# # Taking three inputs at once
# x, y, z = input("Enter three values (e.g., total boys girls): ").split()
# print("Total number of students:", x)
# print("Number of boys is:", y)
# print("Number of girls is:", z)

# #Take  conditional input from user in python 
# # Prompting the user for input
# age_input = input("Enter your age: ")

# # Converting the input to an integer
# age = int(age_input)

# # Checking conditions based on user input
# if age < 0:
#     print("Please enter a valid age.")
# elif age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")


# #Print Names in Python
# color = input("What color is rose?")
# print(color)



# Print Numbers in Python
 
n = int(input("How many roses? "))
print (n)       


# Print Float/Decimal Number in Python

# taking input as float 
# TypeCasting to float
# price = float(input("Price of each roses? "))
# print( price )

# #final datatype of input in python 

# a = "HelLO World"
# b = 10
# c = 11.22
# d = ("Anjali", "Is", "Hero")
# e = ["Geeks", "for", "Geeks"]
# f = {"Geeks": 1, "for":2, "Geeks":3}

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))


# Formatting Output using The Format Method

# Positional formatting with format() method

# Using indexed placeholders for string formatting
print("I love {0} for \"{1}!\"".format("Geeks", "Geeks"))

# {0} is replaced by the first argument 'Geeks'
print("{0} and Portal".format("Geeks"))

# Formatting with placeholders, {0} replaced by 'Geeks'
print("Portal and {0}".format("Geeks"))


# Advanced Usage with Positional and Named Parameters
# Advanced formatting with positional and named arguments

# Mixing positional and named arguments
template = "Number one portal is {0}, {1} and {other}."
print(template.format("Geeks", "For", other="Geeks"))

# Format integers and floats with specified width and precision
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 0.5534))

# Demonstrate order swapping and formatting precision
print("Second argument: {1:3d}, first one: {0:8.2f}".format(47.42, 11))

# Using named arguments for clarity in complex formats
print("Geeks: {a:5d}, Portal: {p:8.2f}".format(a=453, p=59.058))


# Formatting Output using String Method


cstr = "I love geeksforgeeks"

# Printing the center aligned string with fillchr
print("Center aligned: ")
print(cstr.center(40, '#'))

# Printing the left aligned string with "-" padding
print("left aligned: ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string with "-" padding
print("right aligned: ")
print(cstr.rjust(40, '-'))