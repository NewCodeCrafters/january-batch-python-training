# Knight's Quest:
# Create a list representing your knight's equipment including armor, sword, and shield.
# Use list slicing to equip your knight for different types of battles (e.g., full armor for defense, sword and shield for offense).
# Use pop to discard damaged or ineffective equipment after a battle.
# Use insert to replace a broken item with a new one.

# itenaries = ["Armour", "Boots", "Helmet", "Sword", "Bow", "Arrow", "Spear", "Horse"]

# defence = itenaries[:3]
# print(defence)

# offence = itenaries[3:-1]
# print(offence)

# itenaries.pop()

# print(itenaries)
# itenaries.insert(3, "Chariot")

# print(itenaries)

# Space Explorer's Log:
# Create a list representing the planets you've visited during your space exploration.
# Use len to count how many planets you've discovered.
# Use append to add newly discovered planets to your log.
# Use indexing and list slicing to study a specific range of planets in your log.
# planets = ["Earth 22", "Earth X", "Mecury", "Venus", "Mars", "Pluto", "Saturn", "Kratos", "Krypton"]
# print(len(planets))

# print(planets[1::2])
# print(planets[4])

# Pirate's Booty Division:
# Create a list representing the treasures you've plundered.
# Use list slicing to divide your treasure equally among your crew members.
# Use pop to distribute individual treasures to each crew member until the treasure hoard is empty.
# Use extend to add more treasures to your hoard as you raid other ships.

treasures = ["Chest", "Jewelries", "precious Stones", "Gold", "Saphire", "Ruby", "Silver", "Diamond", "Kolonium", "Gold Coins", "platinum", "Tanzanite Stone"]

member1 = treasures[:4]
member2 = treasures[4:8]
member3 = treasures[8:]

print(member1)
print(member2)
print(member3)