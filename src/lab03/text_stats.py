import sys

sys.path.append(r"C:\Users\user\Desktop\python_labs\src")
from lib.normalize_function import normalize
from lib.tokenize_function import tokenize
from lib.count_freq_top_n_function import count_freq, top_n

import io  # инструмент инпут аутпут

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
text = sys.stdin.read().strip()
# text = 'мир, привет!!! привет!!'
print(text)

norm_f = normalize(text)
tokens = tokenize(norm_f)
slovar = count_freq(tokens)  # тип - словарь, используем его в ф-ции top_n
top = top_n(slovar, 5)

print("Всего слов:", len(tokens))
print("Уникальных слов:", len(slovar))
print("Топ-5:")
for slova in top:
    print(slova[0], ":", slova[1])
