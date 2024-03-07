# condtional statements

# name = input("Enter your name here: ")
# age = int(input("How old are you? "))

# print(f"Hello {name}, You are old enough")
# print(f"Hello {name}, You are not old enough")

# if age > 18:
#   print(f"Hello {name}, You are old enough")
# else:
#   print(f"Hello {name}, You are not old enough")

# move_count = int(input("How many moves do you have left: "))

# if move_count == 1:
#   print(f"You have {move_count} move left..")
#   print("Game on")
# elif move_count > 1:
#   print(f"You have {move_count} moves left..")
#   print("Game on")
# else:
#   print(f'You have no moves left')
#   print("Game Over")

# moves = int(input("How many moves do you have left? "))

# if moves < 1:
#   print("Game Over")
# elif moves == 1:
#   print(f"You have {moves} move left")
# else:
#   print(f"You have {moves} moves left")

password = input("Enter Your Password here: ")

if len(password) < 8:
  print("Password too Simple. Minimum password length is 8")
elif len(password) > 30:
  print("Password is too long. Maximum password length is 15")
else:
  print("Password is safe to use.")
  
