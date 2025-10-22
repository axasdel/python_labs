tokens = ["bb","aa","bb","aa","cc"]

def count_freq(tokens):
    dict_token = {}
    for token in tokens:
        frequence = tokens.count(token)
        dict_token[token] = frequence
    return dict_token

slovar = count_freq(tokens) #словарь
print(slovar)

def top_n(slovar, n):
    spisok = []
    for key, value in slovar.items():
        spisok.append((key, value))
    for i in range(len(spisok)):
        for j in range(i + 1, len(spisok)):
            if spisok[i][0] > spisok[j][0]:
                spisok[i], spisok[j] = spisok[j], spisok[i]
    for i in range(len(spisok)):
        for j in range(i + 1, len(spisok)):
            if spisok[i][1] < spisok[j][1]:
                spisok[i],spisok[j] = spisok[j], spisok[i]
    return spisok[:n]
print(top_n(slovar, 2))