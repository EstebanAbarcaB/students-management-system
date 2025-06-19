from actions.insert_students_info import insert_students

option = 0

print('\nWelcome to the student management system.\n\nPlease choose one of the following options: \n')
option = int(input('1. Add student(s)\n2. Check all the available students\n3. Check the top 3 students with the best averages\n4. Check the average among all students\n5. Export the information into a CSV file\n6. Import information from a CSV'))

if option == 1:
    insert_students.insert_students()