import json
from src.lab08.models import Student


def students_to_json(students, path):
    students = [student.to_dict() for student in students]

    with open(path, 'w', encoding='utf-8') as jf:
        json.dump(students, jf, ensure_ascii=False, indent=2)


def students_from_json(path):
    with open(path, 'r', encoding='utf-8') as jf:
        students_d = json.load(jf)
    
    dict_to_student = [Student.from_dict(dictionary) for dictionary in students_d]
    return dict_to_student