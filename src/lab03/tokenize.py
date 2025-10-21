from normalize import normalize
from string import ascii_letters
import re

text = normalize('333 yfhm ^^^')
alphabet = ascii_letters 

def tokensize(text):
    clean_str = re.sub(rf'[^0-9{alphabet}]', ' ', text)
    new_text = clean_str.split()
    return new_text
print(tokensize(text))