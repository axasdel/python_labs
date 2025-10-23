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