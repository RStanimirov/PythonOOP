def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper

# @uppercase
# def input_text():
#     return "Hello World"
#
#
# print(input_text())


# def say_hi():
#     return 'hello there'
#
#
# decorate = uppercase(say_hi)
# print(decorate())


# @uppercase
# def say_hi():
#     return 'hello there'
#
#
# print(say_hi()) # HELLO THERE
