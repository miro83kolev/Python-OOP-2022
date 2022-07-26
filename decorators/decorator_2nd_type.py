#decorators from 2nd type - no parameters in inner function
#3 nested functions, 1st descirbes the parameter of the decorator
def repeat(n): # accepts the argument
    def decorator(function): # defines reference
        def wrapper():
            for _ in range(n):
                function()
        return wrapper
    return decorator


@repeat(4)
def say_hi():
    print('Hello')

say_hi()
#same actions as below long syntax
# repeat(4)(say_hi)()

