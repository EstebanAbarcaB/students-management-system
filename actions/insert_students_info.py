import csv

# def insert_students():
# path = 'P:/Lyfter/repos/students-management-system/files/students_info.csv'

def insert_students():

    students = []
    new_student = 0
    name_and_averageGrade = []
    top_3_students = []

    while True:
        print('This is the current list of students:\n')

        if not students:
            print('No students have been added yet.')
        else:
            for student in students:
                for key, value in student.items():
                    print(f'{key}: {value}')
                print('-------------------------')

        print('\n')
        print("Let's add the student!\n")

        try:
            students_tmp = {}
            students_tmp['Name'] = input('Complete name of the student: ')
            print('\n')
            students_tmp['Classroom'] = input('Classroom: ')
            print('\n')

            while True:
                try:
                    spanish_grade = int(input("Spanish grade: "))
                    if spanish_grade >= 0 and spanish_grade<= 100:
                        students_tmp['Spanish grade'] = spanish_grade
                        break
                    else:
                        print('Grade must be within 0 and 100.\n')
                except ValueError as e:
                    print('Invalid value.\n')
            print('\n')

            while True:
                try:
                    english_grade = int(input("English grade: "))
                    if english_grade >= 0 and english_grade<= 100:
                        students_tmp['English grade'] = english_grade
                        break
                    else:
                        print('Grade must be within 0 and 100.\n')
                except ValueError as e:
                    print('Invalid value.\n')
            print('\n')

            while True:
                try:
                    socialStudies_grade = int(input("Social studies grade: "))
                    if socialStudies_grade >= 0 and socialStudies_grade<= 100:
                        students_tmp['Social studies grade'] = socialStudies_grade
                        break
                    else:
                        print('Grade must be within 0 and 100.\n')
                except ValueError as e:
                    print('Invalid value.\n')
            print('\n')

            while True:
                try:
                    science_grade = int(input("Science grade: "))
                    if science_grade >= 0 and science_grade<= 100:
                        students_tmp['Science grade'] = science_grade
                        break
                    else:
                        print('Grade must be within 0 and 100.\n')
                except ValueError as e:
                    print('Invalid value.\n')
            print('\n')

            students_tmp['Average grade'] = (spanish_grade + english_grade + socialStudies_grade + science_grade) / 4

            
            students.append(students_tmp)


            print('This is the new student:\n')
            for key, value in students_tmp.items():
                print(f'{key}: {value}')
            
            print('\n')
        except ValueError as e:
            print('Invalid value.')

        try:
            new_student = int(input('Type 1 if you would like to add another student, otherwise type anything to quit:\n'))
            if new_student != 1:
                print('This is the current list of students:\n')
                for student in students:
                    for key, value in student.items():
                        print(f'{key}: {value}')
                print('-------------------------')
                break
        except ValueError as e:
            print('This is the current list of students:\n')
            for student in students:
                for key, value in student.items():
                    print(f'{key}: {value}')
                print('-------------------------')
            break

    name_and_averageGrade = [{'Name' : student['Name'], 'Average grade' : student['Average grade']} for student in students]
    
    top_3_students = sorted(name_and_averageGrade, key = lambda x : x ['Average grade'], reverse = True) [:3]

    for student in top_3_students:
        print(f"{student['Name']}: {student['Average grade']}")




insert_students()