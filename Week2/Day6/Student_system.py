# Student Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    students[roll] = {
        "Name": name,
        "Course": course,
        "Marks": marks
    }

    print("Student added successfully.\n")


def view_students():
    if not students:
        print("No student records found.\n")
    else:
        for roll, details in students.items():
            print("Roll No:", roll)
            for key, value in details.items():
                print(key + ":", value)
            print("--------------------")


def update_student():
    roll = input("Enter Roll Number to update: ")

    if roll in students:
        students[roll]["Name"] = input("Enter New Name: ")
        students[roll]["Course"] = input("Enter New Course: ")
        students[roll]["Marks"] = input("Enter New Marks: ")
        print("Student updated successfully.\n")
    else:
        print("Student not found.\n")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")


# Menu-driven program
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")