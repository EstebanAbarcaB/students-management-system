from actions.insert_students_info import insert_students
from actions.handle_students import (
    display_all_students,
    get_top_3_students,
    get_average_of_averages
)
from data.read_file import export_students_to_csv, get_all_students

def trigger_menu():
    students = []  
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
            option = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            new_students = insert_students()
            students.extend(new_students)

        elif option == 2:
            display_all_students(students)

        elif option == 3:
            get_top_3_students(students)

        elif option == 4:
            get_average_of_averages(students)

        elif option == 5:
            if not students:
                print("No students to export.")
            else:
                export_students_to_csv(students)
                print("Data successfully exported to CSV.")

        elif option == 6:
            loaded = get_all_students()
            if not loaded:
                print("No CSV file found or it’s empty.")
            else:
                students = loaded
                print("Data successfully imported from CSV.")
                display_all_students(students)

        elif option == 7:
            print("Thanks for using the system. Bye!")
            break

        else:
            print("Invalid option. Please try again.")
