# File Based Record System

FILENAME = "records.txt"

# Add Record
def add_record():
    with open(FILENAME, "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        file.write(roll + "," + name + "," + marks + "\n")
    print("Record added successfully.\n")


# View All Records
def view_records():
    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()
            if not records:
                print("No records found.\n")
            else:
                print("\n--- Student Records ---")
                for record in records:
                    roll, name, marks = record.strip().split(",")
                    print("Roll:", roll, "| Name:", name, "| Marks:", marks)
                print()
    except FileNotFoundError:
        print("File not found.\n")


# Search Record
def search_record():
    roll_search = input("Enter Roll Number to search: ")
    found = False

    try:
        with open(FILENAME, "r") as file:
            for record in file:
                roll, name, marks = record.strip().split(",")
                if roll == roll_search:
                    print("Record Found:")
                    print("Roll:", roll, "| Name:", name, "| Marks:", marks)
                    found = True
                    break

        if not found:
            print("Record not found.\n")

    except FileNotFoundError:
        print("File not found.\n")


# Delete Record
def delete_record():
    roll_delete = input("Enter Roll Number to delete: ")
    updated_records = []
    found = False

    try:
        with open(FILENAME, "r") as file:
            for record in file:
                roll, name, marks = record.strip().split(",")
                if roll != roll_delete:
                    updated_records.append(record)
                else:
                    found = True

        with open(FILENAME, "w") as file:
            file.writelines(updated_records)

        if found:
            print("Record deleted successfully.\n")
        else:
            print("Record not found.\n")

    except FileNotFoundError:
        print("File not found.\n")


# Main Menu
while True:
    print("===== File Based Record System =====")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        search_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")