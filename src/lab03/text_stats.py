import sys 
import re

def norm(text):
    return text.casefold()
def yo2e(text): #ё, Ё -> е, Е
    while text.count('ё') >= 1 or text.count('Ё') >= 1:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    return text
def spacing(text):
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
def normalize(text):
    text = spacing(yo2e(norm(text)))
    return text

def tokenize(norm):
    clear_text = re.sub(r'[^(\w+(\-\w+)*)]', ' ', norm) #заменяем все неугодное на пробелы в text
    new_text = clear_text.split() #разделяем по пробелу
    return new_text 

def count_freq(tokens):
    dict_token = {}
    for token in tokens:
        frequence = tokens.count(token)
        dict_token[token] = frequence
    return dict_token #тип - словарь

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

text = sys.stdin.read().strip()
norm_f = normalize(text)
tokens = tokenize(norm_f)
slovar = count_freq(tokens) 
top = top_n(slovar, 5)

print("Всего слов:",len(tokens))
print("Уникальных слов:",len(slovar))
print("Топ-5:")
print(top)
for slova in top:
    print(slova[0], ':', slova[1])