class Laptop:
    def __init__(self, memory, model):
        self.memory = memory
        self.model = model

    @classmethod #cls refers to laptop - class method instance, hardcoded
    def low_ram_laptop(cls):
        return cls(4, "Dell")

    @classmethod #cls calls Laptop
    def high_ram_laptop(cls):
        return cls(32, "Assus")


laptop1 = Laptop.low_ram_laptop() # normal instance
laptop2 = Laptop.high_ram_laptop()
print(laptop1.memory, laptop1.model)
print(laptop2.memory, laptop2.model)