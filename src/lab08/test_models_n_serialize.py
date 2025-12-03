# src/lab08/quick_test.py
"""Быстрый тест для проверки работы"""

from .models import Student
from .serialize import students_to_json, students_from_json
import tempfile
import os

print("=== Быстрая проверка ===")

# 1. Проверка Student
s = Student("Иванов Иван", "2000-05-15", "SE-01", 4.5)
print(f"1. Student: {s}")
print(f"   Age: {s.age()}")

# 2. Проверка to_dict/from_dict
d = s.to_dict()
s2 = Student.from_dict(d)
print(f"2. Dict: {d}")
print(f"   Restored: {s2.fio}")

# 3. Проверка сериализации
students = [s, Student("Петрова", "2001-01-01", "SE-02", 4.8)]

# Временный файл
with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
    tmp_path = f.name

try:
    students_to_json(students, tmp_path)
    print(f"3. Saved to {tmp_path}")

    loaded = students_from_json(tmp_path)
    print(f"   Loaded {len(loaded)} students")

finally:
    if os.path.exists(tmp_path):
        os.remove(tmp_path)

print("=== Проверка завершена ===")
