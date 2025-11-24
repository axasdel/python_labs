import pytest 

from src.lib.normalize_function import normalize
from src.lib.tokenize_function import tokenize
from src.lib.count_freq_top_n_function import count_freq, top_n


@pytest.mark.parametrize(
    "string, expected",
    [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)


def test_normalize(text, expected):
    #прописать ошибку Extention для Value Error
    assert normalize(text) == expected