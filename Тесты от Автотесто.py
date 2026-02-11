def capitalize_message(func):
    def wrapper():
        return func().capitalize()
    return wrapper

def smile(func):
    def wrapper():
        return func() + ':)'
    return wrapper


@smile
@capitalize_message
def say_hello():
    return "hello"

print(say_hello())
