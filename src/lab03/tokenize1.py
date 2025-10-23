from tokenize_function import tokenize
from normalize_function import normalize

text = normalize('emoji 😀 не слово ')
print(tokenize(text))