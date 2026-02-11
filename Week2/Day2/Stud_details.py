# Program to create student dictionary using user input

student = {}

student["Name"] = input("Enter Name: ")
student["Age"] = int(input("Enter Age: "))
student["Course"] = input("Enter Course: ")
student["Roll No"] = input("Enter Roll No: ")
student["Marks"] = int(input("Enter Marks: "))

print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)