# Program to read data from a file

file = open("sample.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()