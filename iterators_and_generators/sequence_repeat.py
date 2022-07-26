class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.pointer = 0 #follows on which index in sequence we are

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer == self.number:
            raise StopIteration
        symbol = self.sequence[self.pointer % len(self.sequence)] # finding the symbol - index % len(sequence)
        self.pointer += 1
        return symbol


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
