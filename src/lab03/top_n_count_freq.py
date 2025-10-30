import sys
sys.path.append(r'C:\Users\user\Desktop\python_labs\src')
from lib.count_freq_top_n_function import count_freq, top_n

tokens = tokens = ["bb","aa","bb","aa","cc"]
slovar = count_freq(tokens)
print(count_freq(tokens), top_n(slovar, 2))