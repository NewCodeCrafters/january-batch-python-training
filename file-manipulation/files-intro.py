# Files Manipulation in Python

# open, close
# open type => r, w, rb, wb, a

file = open('intro.txt', "r")

print(file.readlines())

file.close()

file2 = open('dum.txt', "a")

numbers1 = [30, 40, 50]
numbers = [13, 14, 15, 16, 17, 18]

for i in numbers1:
  file2.write(f"{i}\n")

file2.close()
