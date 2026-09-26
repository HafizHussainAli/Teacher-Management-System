import sqlite3

connection = sqlite3.connect("practice.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS school_students (
    student_id INTEGER PRIMARY KEY,
    name TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    enrollment_date TEXT,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES school_students(student_id)
)
""")

connection.commit()


while True:

    print("\n===== Student Management System =====")
    print("1. Add a student")
    print("2. Search student by ID")
    print("3. Search student by name")
    print("4. Print all Students")
    print("5. Update Srudent")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")

            cursor.execute(
                "INSERT INTO school_students (student_id, name) VALUES (?, ?)",
                (student_id, name)
            )

            connection.commit()

            print("Student added successfully!")

        except sqlite3.IntegrityError:
            print("Error: This student ID already exists.")

        except ValueError:
            print("Error: Student ID must be a number.")

    elif choice == "2":

        try:
            search_id = int(input("Enter student ID to search: "))

            cursor.execute(
                "SELECT student_id, name FROM school_students WHERE student_id = ?",
                (search_id,)
            )

            result = cursor.fetchone()

            if result:
                print("\nStudent found!")
                print("Student ID:", result[0])
                print("Name:", result[1])

            else:
                print("Student not found.")

        except ValueError:
            print("Error: Student ID must be a number.")

    elif choice == "3":
    
        std_name = input("Enter the name of student:")
        
        cursor.execute("SELECT * FROM school_students WHERE name = ?",(std_name,))
        students = cursor.fetchall()
        if students:
            for student in students:
                print("Student ID:", student[0])
                print("Name:", student[1])
        else:
            print("Student not Found!")
    
    elif choice == "4":
        cursor.execute("SELECT * FROM school_students")
        students = cursor.fetchall()
        
        print("\n =====All students=====")
        
        for student in students:
            print("STUDENT ID:" , student[0])
            print("NAME:" , student[1])
        
    elif choice == "5":
        try:    
        
            id = int(input("Enter the id of student: "))
            new_name = input("Enter new name for student:")

            cursor.execute("UPDATE school_students SET name = ? WHERE student_id = ?",(new_name, id))

            if cursor.rowcount > 0:
                connection.commit()
                print("Students updated Successfully!")
            else:
                print("Student not found")    
        
        except ValueError:
            print("ENTER THE CORRECT INFORMATION")
    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

connection.close()