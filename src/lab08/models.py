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
        date_example = r'^\d{4}-\d{2}-\d{2}'
        if not re.match(date_example, self.birthdate):
            raise ValueError("Check your birthdate format. It might contain some mistakes")
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Check your birthday format. It might be invalid")

        if not (0 <= self.gpa <= 10):
            raise ValueError("GPA must be between 0 and 10")

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
    


if __name__ == "__main__":
    student = Student(
        fio="Иванов Иван Иванович",
        birthdate="2000-05-15",
        group="SE-01",
        gpa=4.5
    )
    print("Создание студента:")
    print(student)
    

