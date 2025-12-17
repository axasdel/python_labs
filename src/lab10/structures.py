from collections import deque


class Stack:
    def __init__(self): # хранилище стека
        self._data = []

    def push(self, item): # добавление в конец списка O(1) амортизированно
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError('Стек пуст')
        return self._data.pop()

    def peek(self):
        # возвращение последнего элемента
        if self._data: return self._data[-1]
        # при пустом стеке будетвозвращен None
        else: return None

    def is_empty(self) -> bool:
        if len(self._data) == 0: return True
        return False # возвращаем True, если не пустой список


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self._data:
            return self._data.popleft()
        else: raise IndexError('Пустая очередь')

    def peek(self):
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data
    
    def __len__(self):
        return len(self._data)
