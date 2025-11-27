# ЛАБОРАТОРНЫЕ РАБОТЫ



## ЛАБОРАТОРНАЯ РАБОТА 1

*Задание 1. Блок А*
```python
name  = input('Имя:')
age = int(input('Возраст:'))
new_age = age + 1
print(f'Привет, {name}! Через год тебе будет {new_age}')
```
![img01](https://github.com/axasdel/python_labs/blob/main/src/images/lab01/img01.png)

*Задание 2. Блок А*
```python
a = float(input("a:").replace(',', '.'))
b = float(input("b:").replace(',', '.'))
summa = a + b
avg = str((summa / 2))
if int(avg[3]) >= 5: avg = str(float(avg) + 0.01)
print(f'sum={summa}, avg ={avg[:4]}')
```
![img02](https://github.com/axasdel/python_labs/blob/main/src/images/lab01/img02.png)

*Задание 3. Блок А*
```python
price = float(input('price:'))
discount = float(input('discount:'))
vat = float(input('vat:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки:{base}')
print(f'НДС:{vat_amount}')
print(f'Итого к оплате:{total}')
```
![img03](https://github.com/axasdel/python_labs/blob/main/src/images/lab01/img03.png)

*Задание 4. Блок А*
```python
min = int(input('Минуты:'))
hours = min // 60
minut = min % 60
print(f'{hours}:{minut}')
```
![img04](https://github.com/axasdel/python_labs/blob/main/src/images/lab01/img04.png)

*Задание 5. Блок А*
```python
bio = input('ФИО:')
fio = bio.split()
initials = ''.join([i[0] for i in fio]).upper()
dlina = 0
for l in fio:
    dlina += len(l)
print(f'Инициалы:{initials}.')
print(f'Длина (символов):{dlina + 2}')
```
![img05](https://github.com/axasdel/python_labs/blob/main/src/images/lab01/img05.png)



## ЛАБОРАТОРНАЯ РАБОТА 2

*Задание 1. Блок А*
```python
nums = [1, 3, 2, 3]
def min_max(nums):
    nums_tup = []
    if len(nums) > 0:
        mini = nums_tup.append(min(nums))
        maxi = nums_tup.append(max(nums))
        print(tuple(nums_tup))
    else:
        raise ValueError
min_max(nums)
```
![img01](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img01.png)
![img11](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img11.png)
![img12](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img12.png)

*Задание 2. Блок А*
```python
nums = []
def unique_sorted(nums):
    new_nums = sorted(set(nums))
    print(new_nums)
unique_sorted(nums)
```
![img02](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img02.png)
![img21](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img21.png)
![img22](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img22.png)

*Задание 3. Блок А*
```python
mat = [[1, 2], [3, 4]]
def flatten(mat):
    new_mat = []
    for num in mat:
        if type(num) == tuple or type(num) == list:
            for i in range(len(num)):
                if num[i] != '':
                    new_mat.append(num[i])
        else:
            raise ValueError
    print(new_mat)
flatten(mat)
```
![img03](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img03.png)
![img31](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img31.png)
![img32](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img32.png)

*Задание 1. Блок Б*
```python
mat= [[1, 2], [3, 4]]

def check_rvanost(mat):
    dlina = len(mat[-1])
    for x in mat:
        if len(x) != dlina:
            raise ValueError
        else:
            return True
def transpose(mat):
    if check_rvanost:
        new_mat = []
        for stolbec in range(len(mat[-1])):
            new_row = []
            for row in range(len(mat)):
                new_row.append(mat[row][stolbec])
            new_mat.append(new_row)
    print(new_mat)
transpose(mat)
```
![matrix1](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/matrix1.png)

*Задание 2. Блок Б*
```python
mat = [[1, 2], [3]]
def check_rvanost(mat):
    for i in range(len(mat)):
        if len(mat[i]) == len(mat[i+1]):
            return True
        else:
            return False
def row_sums(mat):
    new_mat = []
    for x in mat:
        if type(x) == list and check_rvanost(mat):
            summa = 0
            for i in range(len(x)):
                summa += x[i]
            new_mat.append(summa)
        else:
            raise ValueError
    print(new_mat)
row_sums(mat)
```
![matrix2](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/matrix2.png)

*Задание 3. Блок Б*
```pyhon
```
![matrix3](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/matrix3.png)

*Задание 1. Блок С*
```python
mat = [[1, 2], [3]]
def check_rvanost(mat):
    for i in range(len(mat)):
        if len(mat[i]) == len(mat[i+1]):
            return True
        else:
            return False
def row_sums(mat):
    new_mat = []
    for x in mat:
        if type(x) == list and check_rvanost(mat):
            summa = 0
            for i in range(len(x)):
                summa += x[i]
            new_mat.append(summa)
        else:
            raise ValueError
    print(new_mat)
row_sums(mat)
```
![tuples](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/tuples.png)



## ЛАБОРАТОРНАЯ РАБОТА 3

*Задание 1. Блок А*
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    symbols = ['t', 'r', 'n']
    for symb in symbols:
        comb = "\\" + symb
        text = re.sub(rf'{comb}', ' ', text) #заменяем неподходящую комбинацию символов на пробел
    for s in range(len(text)):
        try: 
            if text[s] + text[s+1] == '  ':
                text = text.replace('  ', ' ')
        except IndexError: #при выходе за границы
            break
    text = text.strip() #"схлопываем текст"
    return text
```
![normalize1](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/norm1.png)
![normalize2](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/norm2.png)
![normalize3](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/norm3.png)
![normalize4](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/norm4.png)


*Задание 2. Блок А.*
```python
import re # для использования "шаблонов"

def tokenize(text):
    clear_text = re.sub(r'[^\w\s-]', ' ', text) #заменяем все неугодное на пробелы в text
    new_text = clear_text.split() #разделяем по пробелу
    return new_text #возвращаем список
```
![tokenize1](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/tok1.png)
![tokenize2](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/tok1.png)
![tokenize3](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/tok3.png)
![tokenize4](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/tok4.png)
![tokenize5](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/tok5.png)

*Задание 3. Блок А*
```python
from collections import Counter 

def count_freq(tokens: list):
    dict_token = Counter(tokens) #используем класс counter, подсчитывающий сколько раз каждый элемент входит в массив
    return dict_token

def top_n(slovar, n):
    spisok = []
    for key, value in slovar.items():
        spisok.append((key, value)) #делаем список из кортежей, в кот. помещены ключ и значение 
    for i in range(len(spisok)):
        for j in range(i + 1, len(spisok)):
            if spisok[i][0] > spisok[j][0]: #сравнение ключей по алфавиту
                spisok[i], spisok[j] = spisok[j], spisok[i] 
    for i in range(len(spisok)):
        for j in range(i + 1, len(spisok)):
            if spisok[i][1] < spisok[j][1]: #сравнение частоты
                spisok[i], spisok[j] = spisok[j], spisok[i]
    return spisok[:n] #обрезаем список кортежей
```
![count_freq_top_n1](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/count_freq_top_n1.png)
![count_freq_top_n2](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/count_freq_top_n2.png)

*Блок В*
```python
import sys
sys.path.append(r'C:\Users\user\Desktop\python_labs\src')
from lib.normalize_function import normalize
from lib.tokenize_function import tokenize
from lib.count_freq_top_n_function import count_freq, top_n

import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
text = sys.stdin.read().strip()
print(text)

norm_f = normalize(text)
tokens = tokenize(norm_f)
slovar = count_freq(tokens) #тип - словарь, используем его в ф-ции top_n
slovar = count_freq(tokens) 
top = top_n(slovar, 5)

print("Всего слов:",len(tokens))
print("Уникальных слов:",len(slovar))
print("Топ-5:")
print(top)
for slova in top:
    print(slova[0], ':', slova[1])
```
![text_stats](https://github.com/axasdel/python_labs/blob/main/src/images/lab03/text_statss.png)



## ЛАБОРАТОРНАЯ РАБОТА 4

*Задание 1-2. Блок А*
```python
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
```
![io](https://github.com/axasdel/python_labs/blob/main/src/images/lab04/io_txt_csv.png)

*Блок В*
```python
from pathlib import Path
import csv

import sys
sys.path.append(r'C:\Users\user\Desktop\python_labs\src')
from lib.normalize_function import normalize
from lib.tokenize_function import tokenize
from lib.count_freq_top_n_function import count_freq, top_n


def read_text(path, encoding = 'utf-8'):
    path = Path(path)
    with open(path, 'r', encoding = 'utf-8') as f:
        return f.read()

def report_writer(path, count_f, encoding = 'utf-8'):
    path = Path(path)
    sortirovka = top_n(count_f, len(count_f))
    with open(path, 'w', newline = '', encoding='utf-8') as f:
        csv_maker = csv.writer(f, delimiter=',')
        csv_maker.writerow(('word', 'count'))
        for word, freq in sortirovka:
            csv_maker.writerow((word, freq))

try:
    text_i = read_text('src/data/lab04/input.txt', encoding='utf-8')
    norm = normalize(text_i)
    token = tokenize(norm)
    count_f = count_freq(token) 
    top = top_n(count_f, 5)

    report_writer('src/data/lab04/report.csv',count_f, encoding = 'utf-8')
    print('Всего слов:', len(token))
    print('Уникальных слов:', len(count_f))
    for t in top:
        print(t[0], ':', t[1])
except FileNotFoundError:
    print('Файл не найден')
except UnicodeDecodeError:
    print('Неподходящая кодировка')
```
![report](https://github.com/axasdel/python_labs/blob/main/src/images/lab04/text_report.png)



## ЛАБОРАТОРНАЯ РАБОтА 5

*Задание 1. Реализация JSON <-> CSV*
```python
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
    if not all(isinstance(element, dict) for element in json_text):  # все ли элементы - словари
        raise ValueError("JSON - список словарей")

    fieldnames = list(json_text[0].keys())  # преобразование ключей 1ого словаря в заголовок для будующего csv
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
```
![json_csv](https://github.com/axasdel/python_labs/blob/main/src/images/lab05/json_csv.png)
![csv_json](https://github.com/axasdel/python_labs/blob/main/src/images/lab05/csv_json.png)

*Задание 2. Реализация CSV -> XLSX*
```python
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

from pathlib import Path
import sys

sys.path.append(r"C:\Users\user\Desktop\python_labs\src")


def csv_to_xlsx(csv_path_1, xlsx_path_2):
    csv_newpath = Path(csv_path_1)
    xlsx_newpath = Path(xlsx_path_2)

    if not csv_newpath.exists():
        raise FileNotFoundError("Файла csv не существует")

    workbook = Workbook()  # создание книги эксель
    work_sheet = workbook.active  # активный лист
    work_sheet.title = "Sheet1"

    column_width = {}  # для макс ширины столбца

    with csv_newpath.open("r", encoding="utf-8") as cf:
        csv_reading = csv.reader(cf)
        for row in csv_reading:
            work_sheet.append(row)
            for column_ind, value in enumerate(
                row, start=1
            ):  # enumerate для получения (индекс, значение)
                cell_length = len(value)  # длина значения
                if cell_length > column_width.get(
                    column_ind, 0
                ):  # случай, если длина значения > текущей макс ширины
                    column_width[column_ind] = cell_length

    for column_ind, width in column_width.items():  # для индекса, ширины в словаре
        letter = get_column_letter(
            column_ind
        )  # исходя из индекса, присваеваем столбцам экселевские буквы
        work_sheet.column_dimensions[letter].width = (
            (width + 2) if (width + 2) >= 8 else 8
        )  # по 1 отступу с обеих сторон

    workbook.save(xlsx_newpath)


if __name__ == "__main__":  # запуск напрямую
    csv_path = "src/lab05/data/samples/people.csv"
    xlsx_path = "src/lab05/data/result/res_people.xlsx"
    csv_to_xlsx(csv_path, xlsx_path)
```
![csv_xlsx](https://github.com/axasdel/python_labs/blob/main/src/images/lab05/csv_xlsx.png)



## ЛАБОРАТОРНАЯ РАБОТА 6

*Задание 1. CLI_TEXT*
```python
import argparse
from collections import Counter
from pathlib import Path

import sys
sys.path.append(r"C:\Users\user\Desktop\python_labs\src")
from lib.normalize_function import normalize
from lib.tokenize_function import tokenize
from lib.count_freq_top_n_function import count_freq, top_n


def cat_read_text(path, numeration = 0):
    new_path = Path(path)
    if not new_path.exists():
        raise FileNotFoundError('Файл не найден')

    with open(new_path, 'r', encoding='utf-8') as f:
        if numeration:
            for num, row in enumerate(f, 1):
                print(f'{num}: {row}')
        else:
            print(f.read())



def main(): #основная функция
    parser = argparse.ArgumentParser(description='CLI для работы с текстом') #создание объекта, для присваивания ему аргументов 
    subparsers = parser.add_subparsers(dest='command') #"контейнер" для подкоманд


    #подкоманда cat
    cat_parser = subparsers.add_parser('cat', help = 'Вывести содержимое файла')
    cat_parser.add_argument('--input', required=True)
    cat_parser.add_argument('-n', action='store_true', help = 'Нумеровать строки')

    #подкоманда stats
    stats_parser = subparsers.add_parser('stats', help = 'Частота слов')
    stats_parser.add_argument('--input', required=True)
    stats_parser.add_argument('--top', type=int, default=5) #если пользователь не укажет значение, то оно автоматом будет 5


    args = parser.parse_args()


    if args.command == 'cat': #если подкоманда cat
        try:
            cat_read_text(args.input, args.n)
        except Exception as e:
            parser.error('Ошибка в подкоманде cat')

    if args.command == 'stats': #если подкоманда stats
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                text = f.read()

                norm_f = normalize(text)
                tokens = tokenize(norm_f)
                slovar = count_freq(tokens)  # тип - словарь, используем его в ф-ции top_n
                top = top_n(slovar, args.top)

                print("Всего слов:", len(tokens))
                print("Уникальных слов:", len(slovar))
                print(f"Топ-5: {args.top}")
                for slova in top:
                    print(slova[0], ":", slova[1])
        except Exception as e:
            parser.error('Ошибка в подкоманде stats')


if __name__ == '__main__':
    main()
```
![cat](https://github.com/axasdel/python_labs/blob/main/src/images/lab06/cat_test.png)
![stats](https://github.com/axasdel/python_labs/blob/main/src/images/lab06/stats_test.png)

*Задание 2. CLI_CONVERT*
```python
import argparse
import json
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from pathlib import Path

import sys
sys.path.append(r"C:\Users\user\Desktop\python_labs\src")


def csv2xlsx(csv_path_1, xlsx_path_2):
    csv_newpath = Path(csv_path_1)
    xlsx_newpath = Path(xlsx_path_2)

    if not csv_newpath.exists():
        raise FileNotFoundError("Файла csv не существует")

    workbook = Workbook()  # создание книги эксель
    work_sheet = workbook.active  # активный лист
    work_sheet.title = "Sheet1"

    column_width = {}  # для макс ширины столбца

    with csv_newpath.open("r", encoding="utf-8") as cf:
        csv_reading = csv.reader(cf)
        for row in csv_reading:
            work_sheet.append(row)
            for column_ind, value in enumerate(row, start=1):  # enumerate для получения (индекс, значение)
                cell_length = len(value)  # длина значения
                if cell_length > column_width.get(column_ind, 0):  # случай, если длина значения > текущей макс ширины
                    column_width[column_ind] = cell_length

    for column_ind, width in column_width.items():  # для индекса, ширины в словаре
        letter = get_column_letter(column_ind)  # исходя из индекса, присваеваем столбцам экселевские буквы
        work_sheet.column_dimensions[letter].width = ((width + 2) if (width + 2) >= 8 else 8)  # по 1 отступу с обеих сторон

    workbook.save(xlsx_newpath)


def json2csv(json_path, csv_path):
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
    if not all(isinstance(element, dict) for element in json_text):  # все ли элементы - словари
        raise ValueError("JSON - список словарей")

    fieldnames = list(json_text[0].keys())  # преобразование ключей 1ого словаря в заголовок для будующего csv
    with csv_newpath.open("w", encoding="utf-8", newline="") as cf:
        csv_writer = csv.DictWriter(cf, fieldnames=fieldnames, extrasaction="ignore")
        csv_writer.writeheader()  # игнорирование лишних ключей
        csv_writer.writerows(json_text)


def csv2json(csv_path, json_path):
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


def main():
    parser = argparse.ArgumentParser(description='CLI для конвертации файла')
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')


    #подкоманда json2csv
    json2csv_parser = subparsers.add_parser('json2csv', help='JSON -> CSV')
    json2csv_parser.add_argument('--in', required=True, dest='input_file', help='Входной JSON')
    json2csv_parser.add_argument('--out', required=True, dest='output_file', help='Выходной CSV')


    #подкоманда csv2json
    csv2json_parser = subparsers.add_parser('csv2json', help='CSV -> JSON')
    csv2json_parser.add_argument('--in', required=True, dest='input_file', help='Вхдной CSV')
    csv2json_parser.add_argument('--out', required=True, dest='output_file', help='Выходной JSON')


    #подкоманда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser('csv2xlsx', help='CSV -> XLSX')
    csv2xlsx_parser.add_argument('--in', required=True, dest='input_file', help='Входной CSV')
    csv2xlsx_parser.add_argument('--out', required=True, dest='output_file', help='Выходной XLSX')


    args = parser.parse_args()


    try:
        if args.command == 'json2csv':
            json2csv(args.input_file, args.output_file)
        elif args.command == 'csv2json':
            csv2json(args.input_file, args.output_file)
        elif args.command == 'csv2xlsx':
            csv2xlsx(args.input_file, args.output_file)
    except Exception as e:
        parser.error


if __name__ == '__main__':
    main()
```
![out_files](https://github.com/axasdel/python_labs/blob/main/src/images/lab06/out_files.png)



## ЛАБОРАТОРНАЯ РАБОТА 7
```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(  # подготовка параметров
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),  # пустые строки
        ("  ", ""),  # пустые строки с пробелами
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected  # проверка


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),  # пустые строки
        ("!@#$%^&*()", []),  # спецсимволы
        ("  ", []),  # пустая строка с пробелами
    ],
)
def test_tokenize(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        ([], {}),  # пустые списки
    ],
)
def test_count_freq(source, expected):
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "source, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
        ({}, 5, []),  # пустые словари
    ],
)
def test_top_n(source, n, expected):
    assert top_n(source, n) == expected
```
1[res](https://github.com/axasdel/python_labs/blob/main/src/images/lab07/res_test_text.png)


```python
import pytest

import json
import csv
from src.lib.file_converting import json_to_csv, csv_to_json


@pytest.fixture  # создаем тест-файл при помощи фикстуры
def sample_json(tmp_path):
    json_newfile = tmp_path / "people.json"  # создаем тест-файл
    text = [
        {"name": "Alice", "age": 25, "city": "Moscow"},
        {"name": "Bob", "age": 30, "city": "Saint Petersburg"},
        {"name": "Marie", "age": 28, "city": "Novosibirsk"},
    ]
    with open(json_newfile, "w", encoding="utf-8") as jf:
        json.dump(text, jf, ensure_ascii=False)
    return json_newfile  # возвращаем путь к созданному тест-файлу


@pytest.fixture
def sample_csv(tmp_path):
    csv_newfile = tmp_path / "people.csv"
    text = [
        ["name", "age", "city"],
        ["Alice", "25", "Moscow"],
        ["Bob", "30", "Saint Petersburg"],
        ["Marie", "28", "Novosibirsk"],
    ]
    with open(csv_newfile, "w", encoding="utf-8", newline="") as cf:
        csv_writer = csv.writer(cf)
        csv_writer.writerows(text)
    return csv_newfile


def test_json_to_csv(sample_json, tmp_path):
    csv_file = tmp_path / "people_from_jf.csv"

    json_to_csv(str(sample_json), str(csv_file))  # JSON -> CSV
    assert csv_file.exists()  # существует ли файл

    with open(csv_file, "r", encoding="utf-8") as cf:
        csv_reader = csv.DictReader(cf)
        rows = list(csv_reader)

        assert len(rows) == 3  # проверка данных
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "25"
        assert rows[0]["city"] == "Moscow"


def test_csv_to_json(sample_csv, tmp_path):
    json_file = tmp_path / "people_from_cf.json"

    csv_to_json(str(sample_csv), str(json_file))
    assert json_file.exists()

    with open(json_file, "r", encoding="utf-8") as jf:
        json_reader = json.load(jf)

        assert len(json_reader) == 3
        assert json_reader[0]["name"] == "Alice"
        assert json_reader[0]["age"] == "25"
        assert json_reader[0]["city"] == "Moscow"
```
![res2]((https://github.com/axasdel/python_labs/blob/main/src/images/lab07/res_test_json_csv.png)