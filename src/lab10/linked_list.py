class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        # добавить элемент в начало списка
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0:
            raise IndexError("Отрцательный индекс не поддерживается")
        if idx == 0:
            return self.prepend(value)
        if idx == self._size:
            return self.append(value)
        if not(0 <= idx <= self._size):
            raise IndexError('Неверный индекс')

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx):
        if not(0 <= idx < self._size):
            raise IndexError('Некорректный индекс')
        elif idx == 0:
            remove = self.head
            self.head = remove.next
            if self._size == 1:
                self.tail = None
            self._size -= 1
            return
        prev = self.head
        for _ in range(idx - 1):
            prev = prev.next

        removed = prev.next
        prev.next = removed.next
        if removed is self.tail:
            self.tail = prev

        self._size -= 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
