import mysql.connector

# CONNECT DATABASE
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kismatkharab@999", 
        database="internship_db"
    )

    mycursor = mydb.cursor()
    print("Connected to MySQL successfully!")

except mysql.connector.Error as err:
    print("Error:", err)
    exit()

# INSERT 
def insert_student():
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    sql = "INSERT INTO Students (name, course, marks) VALUES (%s, %s, %s)"
    values = (name, course, marks)

    mycursor.execute(sql, values)
    mydb.commit()
    print("Student inserted successfully!")


# SELECT 
def show_students():
    mycursor.execute("SELECT * FROM Students")
    records = mycursor.fetchall()

    print("\n--- Student Records ---")
    for row in records:
        print(row)


# UPDATE 
def update_student():
    student_id = int(input("Enter Student ID to update: "))
    new_marks = int(input("Enter New Marks: "))

    sql = "UPDATE Students SET marks=%s WHERE id=%s"
    values = (new_marks, student_id)

    mycursor.execute(sql, values)
    mydb.commit()
    print("Student updated successfully!")


#  DELETE 
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    sql = "DELETE FROM Students WHERE id=%s"
    value = (student_id,)

    mycursor.execute(sql, value)
    mydb.commit()
    print("Student deleted successfully!")


#  MENU 
while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Insert")
    print("2. Show")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        insert_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")