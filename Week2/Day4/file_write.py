# Program to create a file and write into it

# Open file in write mode
file = open("sample.txt", "w")

# Writing data into file
file.write("Hello, this is a file handling example.\n")
file.write("Python makes file handling easy.\n")
file.write("This file is created using write mode.")

# Close the file
file.close()

print("Data written successfully into sample.txt")