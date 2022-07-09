def get_print_list_func(separator):
    def internal_print(ll):
        # separator makes a closure to parent function
        print(separator.join(str(x) for x in ll))

    return internal_print

print_list = get_print_list_func(' : ')
print_list([1, 2, 3, 4])

