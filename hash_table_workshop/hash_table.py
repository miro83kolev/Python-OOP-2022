from copy import copy


class HashTable:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        self.data = [None] * self.DEFAULT_CAPACITY
        self.free_slots = self.DEFAULT_CAPACITY
        self.count = 0

    def add(self, key, value):
        if self.free_slots == 0:
            self.__grow_data()
        idx = self.__calculate_index(key)
        if self.data[idx] is None:
            self.data[idx] = [(key, value)]
            self.free_slots -= 1
            self.count += 1
            return

        for exist_key, _ in self.data[idx]:
            if key == exist_key:
                raise KeyError(f'{key} already exists!')
        self.data[idx].append((key, value))
        self.count += 1

    def get(self, key):
        idx = self.__calculate_index(key)
        idx_el = self.data[idx]
        if idx_el is None:
            raise KeyError(f'{key} not found!')

        for k, v in idx_el:
            if k == key:
                return v
        raise KeyError(f'{key} not found!')

    def __len__(self):
        return self.count

    def __calculate_index(self, key):
        return hash(key) % len(self.data)

    def __getit(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        try:
            old_value = self.get(key)
            idx = self.__calculate_index(key)
            self.data[idx].remove((key, old_value))
            self.data[idx].append((key, value))
        except KeyError:
            self.add(key, value)

    def remove(self, key):
        idx = self.__calculate_index(key)
        idx_el = self.data[idx]
        if idx_el is None:
            raise KeyError(f'{key} not found!')

        for k, v in idx_el:
            if k == key:
                self.data[idx].remove((k, v))
                self.count -= 1
                return

        raise KeyError(f'{key} not found!')

    def __grow_data(self):
        new_capacity = len(self.data) * 2

        existing_data = copy(self.data)

        self.free_slots = new_capacity

        self.data = [None] * new_capacity
        self.count = 0

        for slot in existing_data:
            for key, value in slot:
                self.add(key, value)


table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table.get('age'))
table.add('Gosho', 23)
print(len(table))
table.remove('Gosho')
table.add('Ivan', 11)
table.add('Stoyan', 17)
table.add('Karim', 16)
table.add('John', 19)
table.add('Darron', 21)
print(len(table))








