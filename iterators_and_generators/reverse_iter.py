class reverse_iter:
    def __init__(self, obj):
        self.obj = obj
        self.start = len(obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= 0:
            current_el = self.obj[self.start]
            self.start -= 1
            return current_el
        else:
            raise StopIteration()


reversed_list = reverse_iter([10 ,1, 2, 3, 4])
for item in reversed_list:
    print(item)

