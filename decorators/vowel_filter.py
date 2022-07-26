#decorators from 1st type - no parameters in inner function

def vowel_filter(function):

    def wrapper():
        # reference
        letters = function()
        return [l for l in letters if l.lower() in 'aeouiy']
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
