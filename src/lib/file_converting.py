import sys

sys.path.append(r"C:\Users\user\Desktop\python_labs\src")
import json
import csv

from pathlib import Path


def json_to_csv(json_path, csv_path):
    json_newpath = Path(json_path)
    csv_newpath = Path(csv_path)

    if not json_newpath.exists():
        raise FileNotFoundError("Файл отсутствует")

    with json_newpath.open("r", encoding="utf-8") as jf:
        json_text = json.load(jf)

    if json_text is None:
        raise ValueError("Файл пуст")
    if len(json_text) == 0:
        raise ValueError("Файл пуст")
    if type(json_text) != list:
        raise ValueError("JSON не список")
    if not all(
        isinstance(element, dict) for element in json_text
    ):  # все ли элементы - словари
        raise ValueError("JSON - список словарей")

    fieldnames = list(
        json_text[0].keys()
    )  # преобразование ключей 1ого словаря в заголовок для будующего csv
    with csv_newpath.open("w", encoding="utf-8", newline="") as cf:
        csv_writer = csv.DictWriter(cf, fieldnames=fieldnames, extrasaction="ignore")
        csv_writer.writeheader()  # игнорирование лишних ключей
        csv_writer.writerows(json_text)


def csv_to_json(csv_path, json_path):
    csv_newpath = Path(csv_path)
    json_newpath = Path(json_path)

    if not csv_newpath.exists():
        raise FileNotFoundError("Файл отсутствует")

    with csv_newpath.open("r", encoding="utf-8", newline="") as cf:
        csv_text = csv.DictReader(cf, delimiter=",")

        if not csv_text.fieldnames:
            raise ValueError("Отсутствуют заголовки")

        text = [dict(row) for row in csv_text]
        if len(text) == 0:
            raise ValueError("Файл пуст")

    with json_newpath.open("w", encoding="utf-8") as jf:
        json.dump(text, jf, ensure_ascii=False, indent=2)
        # отступы


json_path = "src/lab05/data/samples/people.json"
csv_outpath = "src/lab05/data/result/people_from_json.csv"
csv_path = "src/lab05/data/samples/people.csv"
json_outpath = "src/lab05/data/result/people_from_csv.json"

json_to_csv(json_path, csv_outpath)
csv_to_json(csv_path, json_outpath)

