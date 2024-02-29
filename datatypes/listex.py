# The Lost Treasure Hunt:

# Create a list representing a treasure map with locations as elements.
# Use len to find out how many locations are left to explore.
# Use pop to explore the last location on the map.
# Use list slicing to display the first half of the remaining locations.

locations = ["Baghdad", "Nairobi", "Cairo", "California"]

print(len(locations))

last_location = locations.pop()
print(last_location)

print(locations[:2])

# Dragon's Lair Inventory:
# Create an empty list to represent your inventory.
# Use append to add weapons and items you find along your journey.
# Use insert to place a newly found item in a specific spot in your inventory.
# Use extend to add the contents of a treasure chest to your inventory.

inventories = []
inventories.append("Dagger")
inventories.append("Chop Knife")
inventories.append("Spear")
inventories.insert(1, "Gun")
inventories.extend(["Gold", "Diamond", "Bronze", "One Piece"])
last_item = inventories.pop()
even_positioned_items = inventories[::2]
new_positioned_item = inventories[1::2]
print(inventories) 

# Mountain Climber's Gear:
# Create a list representing your climbing gear including ropes, carabiners, and harnesses.
# Use indexing to access and inspect specific items in your gear.
# Use list slicing to pack only the essential gear for a challenging climb.

tools = ["Chalk", "Ropes", "Harnes", "Carabiner"]

print(tools[2])
print(tools[:3])

# Jungle Expedition Supplies:
# Create a list containing supplies for your jungle expedition such as tents, food, and water.
# Use len to check the total number of supplies you have.
# Use pop to remove the last item from your list as you consume it during your journey.
# Use append to add new supplies you discover along the way.

supplies = ["Water", "Food", "Tent", "Chocolate bars", "Match Box", "Kettle", "Dagger", "Cup", "Spoon", "Torch", "Walkie Talkie"]

print(len(supplies))
supplies.pop()
print(supplies)
supplies.append("Map")
print(supplies)