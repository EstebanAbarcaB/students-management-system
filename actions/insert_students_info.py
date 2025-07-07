def insert_students():
    students = []

    while True:
        print('\nCurrent list of students:')
        if not students:
            print('No students added yet.')
        else:
            for student in students:
                for key, value in student.items():
                    print(f'{key}: {value}')
                print('-------------------------')

        print("\nLet's add a new student!\n")

        try:
            student = {}
            student['Name'] = input('Full name of the student: ')
            student['Classroom'] = input('Classroom: ')

            for subject in ['Spanish', 'English', 'Social Studies', 'Science']:
                while True:
                    try:
                        grade = int(input(f'{subject} grade: '))
                        if 0 <= grade <= 100:
                            student[f'{subject} grade'] = grade
                            break
                        else:
                            print('Grade must be between 0 and 100.')
                    except ValueError:
                        print('Invalid input. Please enter a number.')

            student['Average grade'] = (
                student['Spanish grade'] +
                student['English grade'] +
                student['Social Studies grade'] +
                student['Science grade']
            ) / 4

            students.append(student)

            print('\nNew student added:')
            for key, value in student.items():
                print(f'{key}: {value}')

        except Exception as e:
            print(f'An error occurred: {e}')

        try:
            continue_input = int(input('\nType 1 to add another student, or any other number to finish: '))
            if continue_input != 1:
                break
        except ValueError:
            break

    return students
