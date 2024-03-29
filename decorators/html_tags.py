def tags(tag_name):
    def decorator(func_ref):
        def wrapper(*args):
            func_result = func_ref(*args)
            return f'<{tag_name}>{func_result}</{tag_name}>'
        return wrapper
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
