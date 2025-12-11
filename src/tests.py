# Исправленная версия тестов (сохраните как test_pytest.py в src/)

import csv
import tempfile
import pytest
import os
import sys

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Правильные импорты
from lab08.models import Student
from lab09.group import Group

STUDENTS = [
    {
        "fio": "Межеровская Анна Сергеевна",
        "birthdate": "2007-11-04",
        "group": "BIVT-25-4",
        "gpa": 0.01,
    },
    {
        "fio": "Кабанова Амалия Сергеевна",
        "birthdate": "2009-01-18",
        "group": "BIVT-25-4",
        "gpa": 5.0,
    },
    {
        "fio": "Муфазалов Эрик Мансурович",
        "birthdate": "2007-08-28",
        "group": "BIVT-25-4",
        "gpa": 5.0,
    },
]


@pytest.fixture
def group(tmp_path):
    """Создаёт временную группу с тестовыми данными"""
    csv_file = tmp_path / "students.csv"

    with csv_file.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fio", "birthdate", "group", "gpa"])
        for s in STUDENTS:
            writer.writerow([s["fio"], s["birthdate"], s["group"], s["gpa"]])

    return Group(storage_path=str(csv_file))


def test_add(tmp_path):
    """Тест добавления студента"""
    csv_file = tmp_path / "students.csv"
    group = Group(str(csv_file))

    data = STUDENTS[0]
    student = Student(**data)

    group.add(student)
    students = group.list()  # Исправлено: list() вместо get_list()

    assert len(students) == 1

    for field, value in data.items():
        assert getattr(students[0], field) == value


def test_list(group):
    """Тест получения списка студентов"""
    students = group.list()  # Исправлено: list() вместо get_list()

    assert len(students) == len(STUDENTS)

    for i, s in enumerate(STUDENTS):
        assert students[i].fio == s["fio"]
        assert students[i].birthdate == s["birthdate"]
        assert students[i].group == s["group"]
        assert students[i].gpa == s["gpa"]


def test_find(group):
    """Тест поиска студентов"""
    target = STUDENTS[0]

    part = target["fio"].split()[1][:3]
    res = group.find(part)
    assert any(r.fio == target["fio"] for r in res)

    keyword = "серг"
    res2 = group.find(keyword)
    assert len(res2) == sum("серг" in s["fio"].lower() for s in STUDENTS)


def test_update(group):
    """Тест обновления студента"""
    target = STUDENTS[0]
    new_gpa = target["gpa"] + 1

    group.update(target["fio"], gpa=new_gpa)
    updated = group.find(target["fio"])

    assert len(updated) == 1
    assert updated[0].gpa == new_gpa


def test_remove(group):
    """Тест удаления студента"""
    target = STUDENTS[1]

    group.remove(target["fio"])
    students = group.list()  # Исправлено: list() вместо get_list()

    assert len(students) == len(STUDENTS) - 1
    assert all(s.fio != target["fio"] for s in students)
