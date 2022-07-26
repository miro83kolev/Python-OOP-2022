def first_n(n):
    num = 0 # first num
    while num < n:
        yield num
        num += 1 # 0 + 1 and so on


sum_first_n = sum(first_n(5))
print(sum_first_n)

#yield is the opposite of return does not terminate program immediately
#generator is a function
#yield like return returns value


def my_gen():
    # 1
    n = 1
    print('This is printed first')
    yield n
    # 1

    # 1 + 1
    n += 1
    print('This is printed second')
    yield n
    # 2

    # 2 + 1
    n += 1
    print('This is printed at last')
    yield n
    # 3


for num in my_gen():
    print(f'outside generator n = {num}')
