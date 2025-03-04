from typing import List

class StaticArray:
    def __init__(self, capacity: int):
        self.array = [None] * capacity

    def set(self, index: int, value: int) -> None:
        self.array[index] = value

    def get(self, index: int) -> int:
        return self.array[index]

class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value: int) -> None:
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        del self.array[index]

    def get(self, index: int) -> int:
        return self.array[index]

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int) -> None:
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def insert(self, position: int, value: int) -> None:
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if not current:
                return
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def delete(self, value: int) -> None:
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    def find(self, value: int) -> Node:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        return self.head is None

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        current = self.head
        while current and current.next:
            current = current.next
        return current

# Sorting Algorithms

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
