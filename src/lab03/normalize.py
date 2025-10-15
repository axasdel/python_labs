text = r'  двойные   пробелы  '

def norm(text):
    return text.casefold()
# print(norm(text))

def yo2e(text):
    if text.count('ё') >= 1 or text.count('Ё') >= 1:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    return text
# print(yo2e(text))

def spacing(text):
    symbols = ['t', 'r', 'n']
    for symb in symbols:
        comb = "\\" + symb
        if text.count(comb) >= 1:
            text = text.replace(comb, ' ')
    for s in range(len(text)):
        try:
            if text[s] + text[s+1] == '  ':
                text = text.replace('  ', ' ')
        except:
            pass
    text = text.strip()
    return text
# print(spacing(text))

def normalize(text):
    text = spacing(yo2e(norm(text)))
    print(text)
normalize(text)