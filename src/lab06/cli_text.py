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