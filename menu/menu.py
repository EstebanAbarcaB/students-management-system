from actions import insert_students_info
from actions import handle_students
from data import read_file

def trigger_menu():
    while True:
        print("\n==== STUDENT MANAGEMENT SYSTEM MENU ====")
        print("1. Add student information")
        print("2. View all students")
        print("3. View top 3 students by average grade")
        print("4. View overall average grade")
        print("5. Export data to CSV")
        print("6. Import data from CSV")
        print("7. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            students = insert_students_info.insert_students()
            for student in students:
                read_file.add_student(student)

        elif choice == 2:
            students = read_file.get_all_students()
            handle_students.display_all_students(students)

        elif choice == 3:
            students = read_file.get_all_students()
            handle_students.get_top_3_students(students)

        elif choice == 4:
            students = read_file.get_all_students()
            handle_students.get_average_of_averages(students)

        elif choice == 5:
            print("Data is automatically exported when adding a student.")

        elif choice == 6:
            students = read_file.get_all_students()
            if students:
                print("Data successfully imported from CSV.\n")
                handle_students.display_all_students(students)
            else:
                print("No CSV file found or it's empty.")

        elif choice == 7:
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
