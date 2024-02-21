# Lists Operators

# lists are orderable
#  can be indexed and sliced
# arbitrary
# List can be modified
# list can be added

fruits = ["Pawpaw", "Mango", "Berry"]

# print(fruits)

fruits = fruits + ['Banana', "Grape", "Tangerine"]
fruits += ["Kiwi", "Plum"]
# print(fruits)


# append, extend, pop
fruits.append("Tomato")

fruits.extend(["Cucumber", "Water Melon"])

# print(fruits)


fruits.pop()

# print(fruits)

# Exercise: List Operations

# 1. Create a list named `foods` and store 3 well known african dish in the list

# 2. I need you to add 2 english delicacies to the list
# 3. Add 1 asian dish to the foods
# 4. Add your favorite drink to foods
# 5. Oops! You made a mistake. Now remove your favorite drink from the foods list
# 6. Print the output

foods = ["Egusi", "Amala", "Jollof"]

foods.extend(['Waffles', "Beans"])
foods.append('Sushi')
foods.append("Chocolate Ice Cream")

foods.pop()
# len() operator
# lists are mutable

# print(foods)
# print(len(foods)) 
# print(min(foods))
# print(max(foods))

foods[0] = "Yam Porridge"
print(foods)
# foods[2:5] = ["Semovita"]
foods.pop(2)

foods.insert(0, "Pounded Yam")
print(foods)

