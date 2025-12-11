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
        date_example = r"^\d{4}-\d{2}-\d{2}$"  # проверка по структуре (регулярка)
        if not re.match(date_example, self.birthdate):
            raise ValueError(
                "Check your birthdate format. It might contain some mistakes"
            )
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")  # проверка через datetime
        except ValueError as e:
            raise ValueError("Check your birthday format. It might be invalid")

        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA must be between 0 and 5")

    def age(self):
        bd = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()

        age = today.year - bd.year

        if (today.month, today.day) < (
            bd.month,
            bd.day,
        ):  # если в этом году мсяц рождения не наступил
            age -= 1

        return age

    def to_dict(self):  # метод экземпляра. сериализация (атрибуты обьекта -> словарь)
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(
        cls, d: dict
    ):  # метод класса. десериализация (содержимое словарей -> "соедржимое" класса)
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):  # строковое представление
        return f"Студент: {self.fio}\nВозраст: {self.age()}\nГруппа: {self.group}\nGPA: {self.gpa}"


if __name__ == "__main__":  # запуск напрямую из файла, при импорте не отображается
    student = Student(
        fio="Иванов Иван Иваныч", birthdate="2009-01-18", group="БИВТ-25-4", gpa=5
    )
    print("Студентик:")
    print(student)
