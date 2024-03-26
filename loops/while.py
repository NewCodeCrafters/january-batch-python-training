# loops

# loops are iterations of conditions

# infinite loops and finite loops

# for loop => finite loop
# while loop => infinite loop.

# val = "a"

# while val == "a":
#   print('a')
#   print("Hello People")

# num = 5

# while num > 0:
#   print(f"Hello {num}")
#   num -= 1
# else:
#   print("End of Loop")

# num = 1

# while num < 6:
#   print(f"Hello {num}")
#   num += 1
# else:
#   print("Loop Ended")

# Create a game that allows users to input a number and print the even numbers between 1 and the number

number = int(input("Enter any number here: "))

low_val = 1

while low_val <= number:
  print(low_val)
  low_val += 2
