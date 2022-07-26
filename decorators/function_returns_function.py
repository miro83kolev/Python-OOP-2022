def hello_func():
    def say_hi():
        return 'Hi'
    return say_hi # this means returning of reference not calling a function

hello = hello_func()
print(hello()) # accessing the enclosure function by its reference