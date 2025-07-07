import csv
from data.file_path import file_path


def add_student(student_data):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students = list(reader) if reader.fieldnames else []
    except FileNotFoundError:
        students = []

    students.append(student_data)

    with open(file_path, "w", encoding="utf-8", newline='') as new_file:
        if students:
            writer = csv.DictWriter(new_file, fieldnames=students[0].keys())
            writer.writeheader()
            writer.writerows(students)

def get_all_students():
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []
