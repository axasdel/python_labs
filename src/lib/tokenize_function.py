import re  # для использования "шаблонов"


def tokenize(text):
    clear_text = re.sub(
        r"[^\w\s-]", " ", text
    )  # заменяем все неугодное на пробелы в text
    new_text = clear_text.split()  # разделяем по пробелу
    return new_text  # возвращаем список
