# strings concatenation
# format strings => f""
# variable names in f strings will always be represented in quotes.

place = "Supermarket"
name = "Spencer"
groceries = "Bread and Crate of eggs"

sentence = name + " is going to the " + place + "." + " And he got" + groceries + "."

sentence1 = f"{name} is going to the {place}. And he got {groceries}"

print(sentence)
print(sentence1)

# I got a new Nike shoe.

types = "New"
brand = "Nike"
wear = "Shoe"
sentence = "I  got  a " + types + " " + brand + " " + wear + "."
new_sentence = f"I got a {types} {brand} {wear}."
print(new_sentence)
