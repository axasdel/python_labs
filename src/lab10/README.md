# ЛАБОРАТОРНАЯ РАБОТА 10

## КЛАСС STACK И КЛАСС QUEUE
```python
from collections import deque


class Stack:
    def __init__(self): # хранилище стека
        self._data = []

    def push(self, item): # добавление в конец списка
        self._data.append(item)

    def pop(self):
        #удаление с конца
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
            return self._data.popleft() #удаление и возвращение первого элемента
        else: raise IndexError('Пустая очередь') 

    def peek(self):
        #смотрим первый элемент, но не удаляем
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data
    
    def __len__(self):
        return len(self._data)
```

## КЛАСС NODE И КЛАСС SINGLYLINKEDLIST
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value #данные, которые хранятся
        self.next = next #ссылка на следующий узел


class SinglyLinkedList:
    def __init__(self):
        self.head = None #нет начала
        self.tail = None #нет конца
        self._size = 0 #размер - 0

    def append(self, value):
        new_node = Node(value) #создаем узел
        if self.head is None: #если цепочка ничего не содержит
            self.head = self.tail = new_node #начало = конец = появление цепочки
        else:
            assert self.tail is not None #прверка, есть ли конец
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1 #увеличение размера

    def prepend(self, value):
        # добавить элемент в начало списка
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx, value):
        #добавление элемента на опр позицию
        if idx < 0:
            raise IndexError("Отрцательный индекс не поддерживается")
        if idx == 0: #в начало
            return self.prepend(value)
        if idx == self._size: #в конец
            return self.append(value)
        if not(0 <= idx <= self._size):
            raise IndexError('Неверный индекс')

        current = self.head #элемент, который будет перед тем положением, куда вставляется элемент
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node #добавляем сам элемент в след позицию от текущего
        self._size += 1

    def remove_at(self, idx):
        #удаляем элемент с определенной позиции
        if not(0 <= idx < self._size):
            raise IndexError('Некорректный индекс')
        elif idx == 0: #с начала
            remove = self.head
            self.head = remove.next
            if self._size == 1: #если один элемент
                self.tail = None
            self._size -= 1
            return
        prev = self.head #элемент перед удаляемым
        for _ in range(idx - 1):
            prev = prev.next

        removed = prev.next
        prev.next = removed.next
        if removed is self.tail: #если удаляемый элемент - конец
            self.tail = prev

        self._size -= 1

    def __iter__(self): #возможность перебирать цепочку(список)
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self): #размер цепочки
        return self._size

    def __repr__(self): #красивый вывод
        values = list(self)
        return f"SinglyLinkedList({values})"
```