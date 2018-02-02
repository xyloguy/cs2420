class Counter:
    def __init__(self):
        self.__swaps = 0
        self.__comparisons = 0

    def get_swaps(self):
        return self.__swaps

    def set_swaps(self, n):
        self.__swaps += n

    swaps = property(get_swaps, set_swaps)

    def get_compares(self):
        return self.__comparisons

    def set_compares(self, n):
        self.__comparisons += n

    compares = property(get_compares, set_compares)
