class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[self.__size() - 1]

    def is_empty(self):
        return self.__items == []

    def __size(self):
        return len(self.__items)