from pathlib import Path
import csv

def read_text(path, encoding ='utf-8'):
    path = Path(path) #класс предоставляет не только путь к файлу, но и возможность работы с ним
    with open(path, 'r', encoding=encoding) as f:
        return f.read()

try:
    text = read_text('src/data/lab04/input.txt', encoding='utf-8')
    print(text)
except FileNotFoundError:
    print('Файл не найден')
except UnicodeDecodeError:
    print('Неподходящая кодировка')


def write_csv(rows, path, header):
    path = Path(path)
    if rows:
        last_dlina = len(rows[-1])
        for row in rows:
            if len(row) != last_dlina:
                raise ValueError
    with open(path, 'w', newline = '', encoding = 'utf-8') as f:
        csv_maker = csv.writer(f, delimiter=',')
        if header:
            csv_maker.writerow(header)
        for row in rows:
            csv_maker.writerow(row)

write_csv([("word","count"),("test",3)], "src/data/check.csv", None)  # создаст CSV
