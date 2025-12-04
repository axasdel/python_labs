def test_correct_student_creation():
    """Проверка создания студента с корректными данными"""
    student = Student(
        fio="Иванов Иван Иванович", birthdate="2000-05-15", group="SE-01", gpa=4.5
    )
    assert student.fio == "Иванов Иван Иванович"
    assert student.birthdate == "2000-05-15"
    assert student.group == "SE-01"
    assert student.gpa == 4.5
    print("✓ Тест 1.1 пройден: Корректное создание студента")
