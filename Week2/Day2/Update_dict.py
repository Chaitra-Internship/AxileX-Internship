# Program to add, update and delete elements in a dictionary

student = {}

# Add elements
student["Name"] = input("Enter Name: ")
student["Age"] = int(input("Enter Age: "))
student["Course"] = input("Enter Course: ")

print("\nDictionary after adding elements:")
print(student)

# Update element
student["Age"] = int(input("\nEnter new Age to update: "))
print("Dictionary after update:")
print(student)

# Delete element
key = input("\nEnter key to delete: ")
student.pop(key, None)

print("Dictionary after deletion:")
print(student)