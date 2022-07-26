def fibonacci():
    fib0 = 0
    fib1 = 1

    yield fib0
    yield fib1

    while True:
        next_number = fib0 + fib1 #creating next number
        yield next_number #yielding it to sequence
        fib0 = fib1 # fib0 becomes fib1
        fib1 = next_number # fib1 becomes next_number and so on


generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
