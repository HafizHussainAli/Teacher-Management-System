import psycopg

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="hussain238"
)

cursor = connection.cursor()

while True:
    print("\n========== Teacher Management System ==========")
    print("1. Add Teacher")
    print("2. View All Teachers")
    print("3. Search Teacher by ID")
    print("4. Search Teacher by Name")
    print("5. Search Teacher by Subject")
    print("6. Update Teacher")
    print("7. Delete Teacher")
    print("8. Activate / Deactivate Teacher")
    print("9. View Active Teachers")
    
    print("10. View Inactive Teachers")
    print("11. Show Highest-Paid Teacher")
    print("12. Show Average Salary")
    print("13. Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        subject = input("Enter subject: ")
        hire_date = input("Enter hire date (YYYY-MM-DD): ")
        salary = input("Enter salary: ")
        cursor.execute("""
            INSERT INTO teachers(first_name, last_name, email, phone, subject, hire_date, salary, is_active)VALUES (%s, %s, %s, %s, %s, %s, %s, TRUE)""", (
            first_name,last_name,email,phone,subject,hire_date,salary))
        connection.commit()
        print("\nTeacher added successfully!")


    elif choice == "2":
        
        cursor.execute("""
            SELECT *
            FROM teachers
            ORDER BY teacher_id""")
        teachers = cursor.fetchall()
        if teachers:

            for teacher in teachers:

                print("\nID:", teacher[0])
                print("First Name:", teacher[1])
                print("Last Name:", teacher[2])
                print("Email:", teacher[3])
                print("Phone:", teacher[4])
                print("Subject:", teacher[5])
                print("Hire Date:", teacher[6])
                print("Salary:", teacher[7])
                print("Active:", teacher[8])
                print("--------------------")

        else:
            print("\nNo teachers found.")

    elif choice == "3":
        teacher_id = input("Enter teacher ID: ")
        cursor.execute("""
            SELECT *
            FROM teachers
            WHERE teacher_id = %s
        """, (teacher_id,))
        teacher = cursor.fetchone()
        if teacher:

            print("\nTEACHER FOUND!")
            print("ID:", teacher[0])
            print("First Name:", teacher[1])
            print("Last Name:", teacher[2])
            print("Email:", teacher[3])
            print("Phone:", teacher[4])
            print("Subject:", teacher[5])
            print("Hire Date:", teacher[6])
            print("Salary:", teacher[7])
            print("Active:", teacher[8])
        else:
            print("\nTeacher not found!")

    elif choice == "4":
        name = input("Enter teacher's name: ")
        cursor.execute("""
            SELECT *
            FROM teachers
            WHERE LOWER(first_name) LIKE LOWER(%s)
            OR LOWER(last_name) LIKE LOWER(%s)
        """, (
            "%" + name + "%",
            "%" + name + "%"
        ))

        teachers = cursor.fetchall()
        if teachers:
            for teacher in teachers:

                print("\nID:", teacher[0])
                print("Name:", teacher[1], teacher[2])
                print("Subject:", teacher[5])
                print("Salary:", teacher[7])
                print("Active:", teacher[8])
                print("--------------------")

        else:
            print("\nTeacher not found!")

    elif choice == "5":
        subject = input("Enter the subject: ")
        cursor.execute("""
            SELECT *
            FROM teachers
            WHERE LOWER(subject) = LOWER(%s)
        """, (subject,))

        teachers = cursor.fetchall()

        if teachers:

            print("\nTEACHERS FOUND!")
            for teacher in teachers:

                print("\nID:", teacher[0])
                print("Name:", teacher[1], teacher[2])
                print("Subject:", teacher[5])
                print("Salary:", teacher[7])
                print("Active:", teacher[8])
                print("--------------------")
        else:
            print("\nNo teacher found for this subject.")

    elif choice == "6":
        teacher_id = input("Enter teacher ID: ")

        cursor.execute("""
            SELECT *
            FROM teachers
            WHERE teacher_id = %s
        """, (teacher_id,))

        teacher = cursor.fetchone()

        if teacher:

            new_firstname = input("Enter new first name: ")
            new_lastname = input("Enter new last name: ")
            new_email = input("Enter new email: ")
            new_phone = input("Enter new phone: ")
            new_subject = input("Enter new subject: ")
            new_salary = input("Enter new salary: ")

            cursor.execute("""
                UPDATE teachers
                SET first_name = %s,
                    last_name = %s,
                    email = %s,
                    phone = %s,
                    subject = %s,
                    salary = %s
                WHERE teacher_id = %s
            """, (
                new_firstname,
                new_lastname,
                new_email,
                new_phone,
                new_subject,
                new_salary,
                teacher_id
            ))

            connection.commit()

            print("\nTeacher updated successfully!")

        else:
            print("\nTeacher not found!")

    elif choice == "7":

        teacher_id = input("Enter teacher ID to delete: ")

        cursor.execute("""
            SELECT *
            FROM teachers
            WHERE teacher_id = %s
        """, (teacher_id,))

        teacher = cursor.fetchone()
        if teacher:
            confirm = input(
                "Are you sure you want to delete this teacher? (yes/no): "
            ).lower()

            if confirm == "yes":

                cursor.execute("""
                    DELETE FROM teachers
                    WHERE teacher_id = %s
                """, (teacher_id,))

                connection.commit()

                print("\nTeacher deleted successfully!")

            else:
                print("\nDelete cancelled.")

        else:
            print("\nTeacher not found!")

    elif choice == "8":

        teacher_id = input("Enter teacher ID: ")
        cursor.execute("""
            SELECT is_active
            FROM teachers
            WHERE teacher_id = %s
        """, (teacher_id,))

        teacher = cursor.fetchone()

        if teacher:
            current_status = teacher[0]
            if current_status is True:
                cursor.execute("""
                    UPDATE teachers
                    SET is_active = FALSE
                    WHERE teacher_id = %s
                """, (teacher_id,))
                connection.commit()
                print("\nTeacher has been DEACTIVATED.")

            else:

                cursor.execute("""
                    UPDATE teachers
                    SET is_active = TRUE
                    WHERE teacher_id = %s
                """, (teacher_id,))
                connection.commit()
                print("\nTeacher has been ACTIVATED.")

        else:
            print("\nTeacher not found!")

    elif choice == "9":

        cursor.execute("""
            SELECT *
            FROM teachers
            WHERE is_active = TRUE
            ORDER BY teacher_id
        """)

        teachers = cursor.fetchall()
        if teachers:
            print("\n========== ACTIVE TEACHERS ==========")

            for teacher in teachers:

                print(
                    teacher[0], "|",teacher[1],teacher[2],"|",teacher[5]
                )

        else:
            print("\nNo active teachers found.")


    elif choice == "10":

        cursor.execute("""
            SELECT *
            FROM teachers
            WHERE is_active = FALSE
            ORDER BY teacher_id
        """)

        teachers = cursor.fetchall()

        if teachers:
            print("\n========== INACTIVE TEACHERS ==========")
            for teacher in teachers:
                print(
                    teacher[0],"|",teacher[1],teacher[2],"|",teacher[5]
                )
        else:
            print("\nNo inactive teachers found.")
    elif choice == "11":

        cursor.execute("""
            SELECT *
            FROM teachers
            ORDER BY salary DESC
            LIMIT 1
        """)

        teacher = cursor.fetchone()
        if teacher:
            print("\n========== HIGHEST-PAID TEACHER ==========")
            print("ID:", teacher[0])
            print("Name:", teacher[1], teacher[2])
            print("Subject:", teacher[5])
            print("Salary:", teacher[7])

        else:
            print("\nNo teachers found.")

    elif choice == "12":

        cursor.execute("""
            SELECT AVG(salary)
            FROM teachers
        """)
        average_salary = cursor.fetchone()
        print("\nAverage Salary:", average_salary[0])
    
    elif choice == "13":
        print("\nGOOD BYE!")
        break
    else:
        print("\nInvalid option! Please select a number from 1 to 13.")

cursor.close()
connection.close()

print("Database connection closed.")
