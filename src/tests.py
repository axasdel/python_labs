# Исправленная версия тестов (сохраните как test_pytest.py в src/)

import csv
import tempfile
import pytest
import os
import sys

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest

from src.lab10.structures import Stack


def test_stack_initially_empty():
    s = Stack()
    assert s.is_empty()
    assert len(s) == 0
    assert s.peek() is None


def test_stack_push_and_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    assert len(s) == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()


def test_stack_peek_does_not_remove():
    s = Stack()
    s.push("a")
    assert s.peek() == "a"
    assert len(s) == 1


def test_stack_pop_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
