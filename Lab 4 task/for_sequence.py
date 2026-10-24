# Loop over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# Loop over a string
print("\nCharacters in 'banana':")
for ch in "banana":
    print(ch)

# Loop over range with enumerate (like slide p.6)
print("\nNumbered list:")
for i, fruit in enumerate(fruits):
    print(i, fruit)