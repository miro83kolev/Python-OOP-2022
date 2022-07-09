def get_line(i, n):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + ('* ' * stars_count).strip()


def get_rhombus(n):
    return [get_line(i, n) for i in range(n)] + \
        [get_line(i, n) for i in range(n - 2, -1, -1)]

def print_line(n):
    print(get_line(n - 1, n - 1))

def print_rhombus(n):
    [print(row) for row in get_rhombus(n)]


print_rhombus(4)


def print_rhombus(n):
    for i in range(n):
        spaces_count = n - 1 - i
        stars_count = i + 1
        print(' ' * spaces_count + '* ' * stars_count)
    for i in range(n - 2, - 1, -1):
        spaces_count = n - 1 - i
        stars_count = i + 1
        print(' ' * spaces_count + '* ' * stars_count)

print_rhombus(3)
print_rhombus(4)
