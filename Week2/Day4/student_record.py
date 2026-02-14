# Program to store student record into a file

# Open file in append mode
with open("student_records.txt", "a") as file:
    
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    # Writing data into file
    file.write("Name: " + name + "\n")
    file.write("Roll No: " + roll + "\n")
    file.write("Course: " + course + "\n")
    file.write("Marks: " + marks + "\n")
    file.write("---------------------------\n")

print("Student record saved successfully.")