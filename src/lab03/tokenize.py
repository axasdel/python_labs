from normalize_function import normalize
from string import ascii_letters
import re # для использования "шаблонов"

text = normalize('emoji 😀 не слово')
cyrillic = 'йцукенгшщзхъфывапролджэячсмитьбю'
alphabet = ascii_letters + cyrillic

def tokensize(text):
    clean_str = re.sub(rf'[^0-9{alphabet}]', ' ', text) #замена подходящих элементов через метод регулярных строк re.sub: подходящие под \
                                                        #"шаблон" символы заменяются пробелом, а неподходящие остаются в строке
    new_text = clean_str.split() #разделение по пробелам "чистой строки"
    return new_text
print(tokensize(text))