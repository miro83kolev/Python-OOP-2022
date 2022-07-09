def print_rhombus(n):
    for i in range(n):
        spaces_count = n - 1 - i
        stars_count = i + 1
        print(' ' * spaces_count + '* ' * stars_count)
    for i in range(n - 2, - 1, -1):
        spaces_count = n - 1 - i
        stars_count = i + 1
        print(' ' * spaces_count + '* ' * stars_count)

print_rhombus(4)