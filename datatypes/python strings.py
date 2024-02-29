# Create a program that gets user's name and store the user's input in reverse as a variable name called password
# Output should be

# Your username is name and your password is password

# hint
# name
# password
#

name = input("what is your name  ")
password = f"{name[::-1]}123"

statement = f"your username is {name} and yourpassword is {password} "  
print(statement)
