from collections import Counter 

def count_freq(tokens: list):
    dict_token = Counter(tokens) #используем класс counter, подсчитывающий сколько раз каждый элемент входит в массив
    return dict_token

def top_n(slovar, n=5):
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
