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
