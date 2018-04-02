def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    t = int(n**0.5)
    f = 5
    while f <= t:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6

    return True


class HashTable:
    def __init__(self, datasize):
        arraysize = datasize * 2 + 1
        while not is_prime(arraysize):
            arraysize += 2
        self.array = [None for _ in range(arraysize)]

    def __index(self, item):
        return int(item) % len(self.array)

    def insert(self, item):
        index = self.__index(item)
        while self.array[index] is not None:
            index += 1
            if index >= len(self.array):
                index = 0
        self.array[index] = item

    def retrieve(self, item):
        index = self.__index(item)
        array_item = self.array[index]

        while array_item is not None and int(array_item) != int(item):
            index += 1
            if index >= len(self.array):
                index = 0
            array_item = self.array[index]

        return array_item

    def delete(self, item):
        index = self.__index(item)
        array_item = self.array[index]

        while array_item is not None and int(array_item) != int(item):
            index += 1
            if index >= len(self.array):
                index = 0
            array_item = self.array[index]

        if array_item is None:
            return False

        self.array[index] = None
        return True

    def __iter__(self):
        for item in self.array:
            if item is not None:
                yield item


if __name__ == "__main__":
    h = HashTable(10)
    h.insert(10)
    h.insert(57)
    h.insert(35)
    for item in h:
        print(item)
