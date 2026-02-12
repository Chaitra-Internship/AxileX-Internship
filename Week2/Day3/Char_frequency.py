# Program to count character frequency

string = input("Enter a string: ")

char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("\nCharacter Frequency:")
for key, value in char_count.items():
    print(key, ":", value)