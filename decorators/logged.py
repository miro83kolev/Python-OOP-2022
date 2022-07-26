def logged(function):
    def wrapper(*args):
        function_name = function.__name__
        function_result = function(*args)
        return f'you called {function_name}{args}\nit returned {function_result}'
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
