# condtional statements

# name = input("Enter your name here: ")
# age = int(input("How old are you? "))

# if age < 13:
#   print(f"Hello {name}, You are old enough")
# else:
#   print(f"Hello {name}, You are not old enough")

moves = int(input("How many moves do you have left? "))

if moves < 1:
  print("Game Over")

else:
  print(f"You have {moves} move left")