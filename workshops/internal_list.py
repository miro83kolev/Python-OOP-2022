class ListInternal:
    def __init__(self):
        self.__values = []

    def append(self, value):
        self.__values.append(value)
        return self

    def remove(self, index):
        return self.__values.pop(index)

    def get_index(self, index):
        pass

    def extend(self, iterable):
        pass

    def insert(self, index, value):
        pass

    def pop(self):
        pass

    def clear(self):
        pass

    def index(self, value):
        pass

    def count(self, value):
        pass

    def size(self):
        pass

    def add_first(self, value):
        pass

    def dictionize(self):
        pass

    def move(self, amount):
        pass

    def sum(self):
        pass

    def overbound(self):
        pass

    def underbound(self):
        pass

    def reverse(self):
        pass

    def copy(self):
        pass


    def __iter__(self):
        for value in self.__values:
            yield  value