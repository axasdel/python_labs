import sys

sys.path.append(r"C:\Users\user\Desktop\python_labs\src")
from lib.normalize_function import normalize

text = "  двойные   пробелы  "
print(normalize(text))
