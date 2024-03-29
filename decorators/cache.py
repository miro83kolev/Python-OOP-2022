def cache(func):
    log = {}

    def wrapper(number):
        if number in log:
            return log[number]
        result = func(number)
        log[number] = result

        return result

    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)


