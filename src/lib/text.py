import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    symbols = ["t", "r", "n"]
    for symb in symbols:
        comb = "\\" + symb
        text = re.sub(
            rf"{comb}", " ", text
        )  # заменяем неподходящую комбинацию символов на пробел
    for s in range(len(text)):
        try:
            if text[s] + text[s + 1] == "  ":
                text = text.replace("  ", " ")
        except IndexError:  # при выходе за границы
            break
    text = text.strip()  # "схлопываем текст"
    return text


import re  # для использования "шаблонов"


def tokenize(text):
    clear_text = re.sub(
        r"[^\w\s-]", " ", text
    )  # заменяем все неугодное на пробелы в text
    new_text = clear_text.split()  # разделяем по пробелу
    return new_text  # возвращаем список


from collections import Counter


def count_freq(tokens: list):
    dict_token = Counter(
        tokens
    )  # используем класс counter, подсчитывающий сколько раз каждый элемент входит в массив
    return dict_token


def top_n(slovar, n=5):
    spisok = []
    for key, value in slovar.items():
        spisok.append(
            (key, value)
        )  # делаем список из кортежей, в кот. помещены ключ и значение
    for i in range(len(spisok)):
        for j in range(i + 1, len(spisok)):
            if spisok[i][0] > spisok[j][0]:  # сравнение ключей по алфавиту
                spisok[i], spisok[j] = spisok[j], spisok[i]
    for i in range(len(spisok)):
        for j in range(i + 1, len(spisok)):
            if spisok[i][1] < spisok[j][1]:  # сравнение частоты
                spisok[i], spisok[j] = spisok[j], spisok[i]
    return spisok[:n]  # обрезаем список кортежей
