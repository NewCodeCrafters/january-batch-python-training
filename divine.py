# I am Divine. I love coding and my intructor is the best in town.
aph1 = "I "
aph2 = "am "
aph3 = "spencer. "
aph4 = "I "
aph5 = "love "
aph6 = "coding "
aph7 = "and "
aph8 = "my "
aph9 = "intructor "
aph10 = "is "
aph11 = "the "
aph12 = "best "
aph13 = "in "
aph14 = "town."

sentence = aph1 + aph2 + aph3 + aph4 + aph5 + aph6 + aph7 + aph8 + aph9 + aph10 + aph11 + aph12 + aph13 + aph14
print(sentence)


# Create a program that gets user's name and store the user's input in reverse as a variable name called password
# Output should be

# Your username is name and your password is password

# hint
# name
# password
#

name = input("what is your name ")
password = f"{name[::-1]}@123"

login = f"your username is {name.upper()} and your password is {password}"

print(login)


