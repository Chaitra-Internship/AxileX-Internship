# Program to append data into a file

file = open("sample.txt", "a")   # Open file in append mode

file.write("\nThis line is added using append mode.")
file.write("\nPython file handling is simple.")

file.close()

print("Data appended successfully.")