def display_all_students(students):
    if not students:
        print("No students registered.")
        return

    print("\nList of all students:\n")
    for student in students:
        for key, value in student.items():
            print(f'{key}: {value}')
        print('-------------------------')

def get_average_grade(student):
    return float(student['Average grade'])

def get_top_3_students(students):

    if not students:
        print("No students registered.")
        return

    print("\nTop 3 students by average grade:\n")
    
    sorted_students = sorted(students, key=get_average_grade, reverse=True)[:3]

    for student in sorted_students:
        print(f"{student['Name']}: {student['Average grade']}")

def get_average_of_averages(students):
    if not students:
        print("No students registered.")
        return

    total_avg = sum(float(student['Average grade']) for student in students)
    overall_avg = total_avg / len(students)
    print(f"\nOverall average grade: {overall_avg:.2f}")
