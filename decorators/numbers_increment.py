def number_increment(numbers):

    def increase():
        result = [el + 1 for el in numbers]
        return result
    return increase() # provides the result of increase function

print(number_increment([1, 2, 3]))