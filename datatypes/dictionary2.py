# dictionary

# fruits = ["paw", 'boy', 'a']
# fruits.pop()
# print(fruits)
info = {}

info['fname'] = "Divine"
info["other_names"] = ["Analo", "Python Boss"]
info['age'] = 13

print(info)
# .clear() removes all the items in a dictionary
# info.clear()
# print(info)

print(info.get('fname'))
print(info.get('fname', "Not Found"))

print(info.items())
print(info.keys())
print(info.values())

# Unlike lists and tuples pop() method in dictionary needs a value.
info.pop('ages', "Not Available")
print(info)

# pop item removes both the last key and value
info.popitem()
print(info)
info1 = {
  "age": 24,
  "gender": "Male",
  "Color": "Yellow",
  "height": "5.4"
}

# update is used to merge 2 dictionaries and also update previous keys and values
info.update(info1)
info.update(gender = "Female", Color = "Red")
print(info)
