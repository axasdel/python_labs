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

def report_writer(path, encoding = 'utf-8', header = None):
    path = Path(path)
    sortirovka = top_n(count_f, len(count_f))
    with open(path, 'w', newline = '', encoding='utf-8') as f:
        csv_maker = csv.writer(f, delimiter=',')
        if header:
            csv_maker.writerow(('word', 'count'))
        for word, freq in sortirovka:
            csv_maker.writerows((word, freq))

try:
    text_i = read_text('src/data/input.txt', encoding='utf-8')
    norm = normalize(text_i)
    token = tokenize(norm)
    count_f = count_freq(token) 
    top = top_n(count_f, 5)

    report_writer('src/lab04/data/report.csv', encoding = 'utf-8')
    print('Всего слов:', len(token))
    print('Уникальных слов:', len(count_f))
    for t in top:
        print(t[0], ':', t[1])
except FileNotFoundError:
    print('Файл не найден')
except UnicodeDecodeError:
    print('Неподходящая кодировка')
