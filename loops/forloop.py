# for loop - finite

# i = 5

# while i > 0:
#   print(i)
#   i -= 1

# number = 12

# for dummy in range(1, number+1):
#   print(dummy)

# fruits = ["Pawpaw", 'Mango', "Banana", "Apple", "Watermelon"]

# for a in fruits:
#   print(a)

# name = "Spencer"

# for char in name:
#   print(char)

# Write a program that prints all the even numbers between 1 and 20.

# for dum in range(1, 21):
#   if dum % 2 == 0:
#     print(dum)
#   else:
#     continue

# for dum in range(1, 21, 2):
#   print(dum)


# Write a program that calculates the sum of the squares of all numbers from 1 to a user-(input_number).
# number = int(input("Enter any number here: "))

# total = 0

# for i in range(1, number+1):
#   square = i ** 2
#   total += square

# print(total)


# Write a program that prints a multiplication table for a given number entered by the user.
# number = int(input("Enter any number here: "))

# for i in range(1, 21):
#   product = number * i
#   print(f'{number} times {i} equals {product}')

# for me in range(1, 21):
#   table = number * me
#   print(f'{number} times {me} equals {table}')
# # Write a program that checks if a given string is a palindrome (reads the same backward as forward). (Ignore spaces and capitalization)


# number = int(input("enter any number: "))
# for him in range(1, 19):
#  table = number * him
#  print(f'{number} times {him} equals {table}')

# total = 0

# Write a program that prints the following pattern:

# *
# * *
# * * *
# * * * *
# * * * * *
# number = int(input("enter amount of stars needed: "))

# for i in range(1,21):
#   print("*" * i)

# number = int(input("enter any number: "))
# for i in range(1,21):
#   print("*" * i)



# Write a program that takes a list of numbers and prints the count of positive, negative, and zero numbers in the list.

# numbers = [13, 0, -1, -4, -48, 48, 91, 0, 0, 26, 21]
# total_positive = 0
# total_negative = 0
# total_neutral = 0

# for num in numbers:
#   if num == 0:
#     total_neutral += 1
#   elif num > 0:
#     total_positive += 1
#   else:
#     total_negative += 1

# print(f'There are {total_negative} negative numbers, {total_neutral} neutral numbers and {total_positive} positive numbers in the list')

# Write a program that converts a string of characters to uppercase.
# sentence = "i am a boy"
# upper_sentence = ""

# for two in sentence:
#   upper_sentence += two.upper()

# print(upper_sentence)

# Write a program that removes duplicates from a given list.
# foods = ["Rice", "Beans", "Eba", "Yam", "Rice", "Beans", "Spaghetti", "Amala"]
# new_food_list = []
# for food in foods:
#   if food in new_food_list:
#     continue
#   else:
#     new_food_list.append(food)

# print(new_food_list)

# Write a program that finds the factorial of a number entered by the user (factorial of a number is the product of all positive integers less than or equal to that number).

# number = int(input("Enter any number here: "))
# total = 1

# for i in range(1, number+1):
#   total *= i

# print(total)
shopping_dict = {
  'grocery': ['egg', 'butter', 'bread'],
  'cereals': ["Corn Flakes", "Golden Morn", "Oat"],
  "meat": "Beef",
  "budget": 20000,
}
# print(shopping_dict["meat"])


# for item in shopping_dict:
#   print(shopping_dict[item])

# for k, v in shopping_dict.items():
#   print(k, v)


names = ["Ola", "Ade", "Tolu", "Tayo", "Tunde"]
scores = [39, 47, 98, 75, 65, 89]

# for i in names:
#   print(i)

# for age in ages:
#   print(age)

# for name, score in zip(names, scores):
#   if score > 50:
#     print(f'{name} graduated with {score}')
#   else:
#     continue


# print(list(range(5, 21, 3)))
# print(list(range(10, 101, 5)))

# for i in range(0, 31, 5):
#   if i == 20:
#     continue # skip
#   elif i == 25:
#     break
#   else:
#     print(i)


