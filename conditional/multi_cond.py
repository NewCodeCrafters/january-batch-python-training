# number = int(input("Enter a number here: "))

# if number > 0:
#   print(f'{number} is positive')
# elif number < 0:
#   print(f'{number} is negative')
# else:
#   print(f'{number} is zero')

# number = int(input("Enter a number here: "))

# # 8 % 2 = 0
# if number % 2 == 0:
#   print(f'{number} is even')
# else:
#   print(f'{number} is odd')

# grade = float(input("Enter your grade score here (1-100): "))

# if grade >= 90 and grade <= 100:
#   print("You got an A")
# elif grade >= 80 and grade <= 89:
#   print("You got a B")
# elif grade >= 70 and grade <= 79:
#   print("You got a C")
# elif grade >= 60 and grade <= 69:
#   print("You got a D")
# elif grade < 60 and grade >= 0:
#   print("You got an F")
# else:
#   print("Invalid Score")


subject = input("What is your Favorite Subject: ")
# if subject.upper() == "ENGLISH" or subject.title() == "History":
#   print("You are going to Art Department")
# elif subject.lower() == "mathematics" or "Science" in subject.title():
#   print("You are going to Science Department")
# elif subject.capitalize() == "Business study" or "Accounting" in subject.title():
#   print("You are going to commercial  Department")
# else:
#   print("You can't get a department")

if subject.capitalize() == "Biology" or subject.title() == "Chemistry" or subject.title() == "Physics":
  print("You are going to Science Department")
elif subject.title() == "Accounting" or subject.title() == "Commerce" or subject.title() == "Bookkeeping":
  print("You are going to commercial Department")
elif subject.upper() == "History" or subject.title() == "English" or "Literature" in subject:
  print("You are going to Art Department")
else:
  print("I am sorry I don't know your department")
