# reading and writing files in python
# Context Managers on Files

# file = open('dum.txt', 'r')

# print(file.readlines())

# file.close()

# context manager
# w, r, a
# with open('dum.txt', 'a') as file:
#   items = ['Tade', "Shade", "Tayo", "Debby"]
#   for i in items:
#     file.write(f"{i}\n")
#   print(file)

# read() method is used to read the content of the file by counting the characters when specified. Otherwise it reads the entire the content
# with open('dum.txt', 'r') as file:
#   print(file.read())

# readline() method is used to read a particular line from a file when specified. Otherwise it reads the first line
# with open('dum.txt', 'r') as file:
#   print(file.readline(5))

# # Read all the items but as a list
# with open('dum.txt', 'r') as file:
#   print(file.readlines())

# with open('dum.txt', 'r') as file:
#   contents = file.readlines()
#   with open('tade.txt', 'w') as file2:
#     for i in contents:
#       file2.write(i)

# with open('pluto.txt', 'r') as file:
#   contents = file.readlines()
#   with open('tade.txt', 'a') as file2:
#     for item in contents:
#       file2.write(item)
