import sys
sys.path.append(r'C:\Users\user\Desktop\python_labs\src')
from lib.tokenize_function import tokenize
from lib.normalize_function import normalize


text = normalize('emoji 😀 не слово ')
print(tokenize(text))