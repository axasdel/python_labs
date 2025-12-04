# ЛАБОРАТОРНАЯ РАБОА №8

## КЛАСС STUDENT
```python
from dataclasses import dataclass
from datetime import datetime, date
import re


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        date_example = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_example, self.birthdate):
            raise ValueError("Check your birthdate format. It might contain some mistakes")
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Check your birthday format. It might be invalid")

        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA must be between 0 and 5")

    def age(self):
        bd = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()

        age = today.year - bd.year

        if (today.month, today.day) < (bd.month, bd.day):
            age -= 1

        return age
    

    def to_dict(self):
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }


    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio = d["fio"],
            birthdate = d["birthdate"],
            group = d["group"],
            gpa = d["gpa"]
        )
    

    def __str__(self):
        return f"Студент: {self.fio}\nВозраст: {self.age()}\nГруппа: {self.group}\nGPA: {self.gpa}"
```
![example](https://github.com/axasdel/python_labs/blob/main/src/images/lab08/ex_student.png)


## СЕРИАЛИЗАЦИЯ / ДЕСЕРИАЛИЗАЦИЯ
```pyhton
import json
from src.lab08.models import Student


def students_to_json(students, path): #сериализация
    students = [student.to_dict() for student in students]

    with open(path, 'w', encoding='utf-8') as jf:
        json.dump(students, jf, ensure_ascii=False, indent=2)


def students_from_json(path): #десериализация
    with open(path, 'r', encoding='utf-8') as jf:
        students_d = json.load(jf)
    
    dict_to_student = [Student.from_dict(dictionary) for dictionary in students_d]
    return dict_to_student
```