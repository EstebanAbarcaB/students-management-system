import csv
import insert_students_info
from data import file_path
def write_students_to_file(file_path, data, headers):

    with open(file_path, 'w', encoding= 'utf-8') as students_file:
        writer = csv.DictWriter(students_file, headers)
        writer.writeheader()
        writer.writerows(data)




write_students_to_file(file_path, insert_students_info.students, insert_students_info.students[0].keys())