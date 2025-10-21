tokens = ["bb","aa","bb","aa","cc", 'aa']

def count_freq(tokens):
    dict_token = {}
    for token in tokens:
        frequence = tokens.count(token)
        dict_token[token] = frequence
    return dict_token

slovar = count_freq(tokens) #словарь
print(slovar)

def top_n(slovar, n):
    res = sorted([...])[::-1]
    return res[:n]
    

# print(top_n(slovar))