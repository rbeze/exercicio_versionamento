import functools


def debug(func):
    """Print the function's signature and return value"""


    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Create a list of the positional arguments
        # Use repr() to get a nice string representing each argument
        args_repr = [repr(a) for a in args]
        # Create a list of the keyword arguments. The f-string formats each argument as key=value 
        # where the !r specifier means that repr() is used to represent the value
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        # The lists of positional and keyword arguments is joined together 
        # to one signature string with each argument separated by a comma
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__} ({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    
    
    return wrapper_debug


@debug
def make_greeting(name, age=None):

    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"


make_greeting("Benjamin")
make_greeting("Helena", age=112)


class MyClass:
    

    def method(self):
        return print('instance method called', self)
    

    @classmethod
    def class_method(cls):
        return print('class method called', cls)
    

    @staticmethod
    def static_method():
        return print('static method called')


instancia = MyClass()
instancia.method()
instancia.class_method()
instancia.static_method()