def uppercase(function): #argument a function
    def wrapper():
        result = function() # calls a function
        uppercase_result = result.upper() # turns in to upper string
        return uppercase_result # returns it
    return wrapper # returns wrapper to uppercase

@uppercase #decorator removes implementation below in comments
def say_hi(): # modification of function via uppercase
    return 'Hello'

@uppercase
def say_bye():
    return 'bye'

@uppercase
def buy():
    return 'start buying'

print(say_hi())
print(say_bye())
print(buy())

# decorate = uppercase(say_hi)
# # bye = uppercase(say_bye)
# # buy = uppercase(buy)
# # print(decorate())
# # print(bye())
# # print(buy())
