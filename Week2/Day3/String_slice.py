# Program to demonstrate string slicing

string = input("Enter a string: ")

print("Original String:", string)

# First 5 characters
print("First 5 characters:", string[:5])

# Last 5 characters
print("Last 5 characters:", string[-5:])

# Characters from index 2 to 7
print("Characters from index 2 to 7:", string[2:8])

# Every second character
print("Every second character:", string[::2])

# Reverse the string
print("Reversed string:", string[::-1])