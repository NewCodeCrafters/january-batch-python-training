# Write a Python program to print "Hello, World!" to the console.

# print("Hello, World")

# Create two variables: one that holds a name (string) and another that holds an age (integer). Print a message incorporating these variables, e.g., "John is 30 years old."

# name = "Divine"
# age = 13

# print(f"{name} is {age} years old")

# Perform addition, subtraction, multiplication, and division with two numbers. Print the results for each operation.

# def addition(number1, number2):
#   print(number1 + number2)

# def subtraction(number1, number2):
#   print(number1 - number2)

# def multiplication(number1, number2):
#   print(number1 * number2)

# def division(number1, number2):
#   print(number1 / number2)

# def floor_division(number1, number2):
#   print(number1 // number2)

# def exponent(number1, number2):
#   print(number1 ** number2)


# number1 = int(input("Enter the first number here: "))
# number2 = int(input("Enter the second number here: "))
# symbol = input("Choose a Symbol: e.g + - / * ** // ")




# if symbol == "+":
#   # Call the add function
#   addition(number1, number2)

# elif symbol == "-":
#   subtraction(number1, number2)

# elif symbol == "/":
#   division(number1, number2)
  
# elif symbol == "*":
#   multiplication(number1, number2)

# elif symbol == "//":
#   floor_division(number1, number2)
# elif symbol == "**":
#   exponent(number1, number2)

# else:
#   print("Invalid Symbol")


# Write a Python script that asks the user for their name and their age, then prints a message greeting them and stating how old they are.

# def introduction(name, age):
#   print(f'Welcome {name}. You are {age} years old')

# name = input("Enter your name here: ")
# age = int(input("How old are you? "))


# introduction(name, age)

# Write a Python program that asks the user for a number, then prints whether the number is positive, negative, or zero.

# def check_number(number):
#   if number < 0:
#     print(f"{number} is negative")
#   elif number == 0:
#     print(f"{number} is neutral")
#   else:
#     print(f"{number} is positive")


# number = int(input("Enter the number here: "))

# check_number(number)


# Use a for loop to print numbers from 1 to 10, inclusive.

# for i in range(1, 11):
#   print(i)

# Use a for loop and the range function to print all even numbers between 1 and 20, inclusive.

# for i in range(2, 21):
#   if i % 2 == 0:
#     print(f"{i} is Even Number")
#   else:
#     continue

# Create a list of five fruits. Print the list. Then add a new fruit to the list and print the updated list.

# fruits = ["Banana", "Pawpaw", "Apple", "Mango"]

# print(fruits)
# fruits.append("Watermelon")

# print(fruits)


# Given a list of numbers, write a Python script that prints each number squared.
# numbers = [12, 10, 5, 3]

# squared_numbers = []

# for num in numbers:
#   square = num ** 2
#   squared_numbers.append(square)
#   squared_numbers = sorted(squared_numbers)

# print(squared_numbers)


# info = {
#   "spencer": 91,
#   "Raji": 202,
#   "hakeem": 12,
#   "anne": 95
# }

# for key, value in info.items():
#   print(f'Name is {key} and age is {value}')

# Write a Python program that creates a file named "test.txt", writes "Hello, file!" to it, and then closes the file.

# file = open("test.txt", 'w')

# file.write("Hello, file!")
# file.close()

# with open("test.txt", 'w') as file:
#   file.write("Hello, file!")


