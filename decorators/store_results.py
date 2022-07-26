def store_results(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        with open('./result.txt', 'a') as file:
            file.write(f"Function '{func_ref.__name__}' was called. Result: {func_result}\n")
    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b

add(3, 10)
mult(7, 8)
