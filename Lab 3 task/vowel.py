ch = input("Enter a character: ")

# Convert to lowercase so 'A' and 'a' both work
ch = ch.lower()

if ch in "aeiou":
    print(ch, "is a Vowel")
else:
    print(ch, "is NOT a Vowel")