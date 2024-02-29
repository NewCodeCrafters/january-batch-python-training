# tuples


names = ["AbdulAzeez", "Ayomide", "Ameerah", "Analo", "Ada"]
names1 = ("AbdulAzeez", "Ayomide", "Ameerah", "Analo", "Ada")

# print(type(names))
# print(type(names1))
names[1] = "Emeka"

print(names)
# tuples can be indexed and are orderable, sliced
names1 = list(names1)
names1.append("Adams")
names1 = tuple(names1)
print(names1)
# print(names[1])
# print(names1[1])
# print(names1[::2])
