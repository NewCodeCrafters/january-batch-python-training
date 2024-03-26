# Define a function
def greet_people(name):
  print(f"Hello {name}")


# greet_people("Hakeem")
# greet_people("Mrs. Raji")


def get_rectangle_area(length, breadth):
  area = length * breadth
  print(f"The area of length {length} and breadth {breadth} is {area}")


# get_rectangle_area(13, 12)


def check_even_or_odd(number):
  if number % 2 == 0:
    print(f"{number} is even")
  else:
    print(f'{number} is odd')


# check_even_or_odd(29)
# check_even_or_odd(35)
# check_even_or_odd(22)

# Write a function that multiplies all the elements in a list of numbers.


def multiply_list(numbers):
  product = 1
  for i in numbers:
    product = product * i
  print(f"The product of {numbers} is {product}")


# multiply_list([2, 3, 0, 5, 6])


def reverse_string(word):
  rev_word = word[::-1]

  print(f"The reverse of {word} is {rev_word}")


# reverse_string("aeiou")
# reverse_string("spencer")


# mom, dad, racecar, bob
def is_palindrome(word):
  rev_word = word[::-1]
  if word.lower() == rev_word.lower():
    print(f'{word} is a palindrome')
  else:
    print(f'{word} is not a palindrome')


# is_palindrome("Tola")
# is_palindrome("peep")


# median
def get_median(numbers):
  sorted_number = sorted(numbers)
  list_length = len(numbers)
  if list_length % 2 == 1:
    position = list_length // 2
    median = sorted_number[position]
    print(median)
  else:
    position1 = (list_length // 2) - 1
    position2 = list_length // 2
    median = (sorted_number[position1] + sorted_number[position2]) / 2
    print(median)


get_median([12, 13, 2, 1, 9, 3])
# dum = [12, 13, 2, 1, 9]

# length_list = len(dum)
# print(length_list)
# print(length_list // 2)

# print(sorted(dum))

#

# mean()
# 9+2+3+4+16 sum(numbers)


def get_mean(numbers):
  total_sum = sum(numbers)
  total_length = len(numbers)
  mean = total_sum / total_length
  print(f'The Mean Average for {numbers} is {mean}')


# / 5 len(numbers)

# mode
# highest


def get_mode(numbers):
  highest = 0
  for i in numbers:
    if i > highest:
      highest = i
  print(f'{highest} is the mode in {numbers}')


get_mode([13, 12, 9, 25, 22])
