"""
    Learn how to write and use a decorator
"""


def now():
    print("2017-6-7")


def log(func):
    def wrapper(*args, **kwargs):
        print("func_name:%s" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log
def wrapper_now():
    print("2017-6-7")


@log
def wrapper_args(param):
    print(param)


def add_title(result):
    return "*******%s********" % result


def aspect_decorator(func):
    def wrapper(*args, **kwargs):
        print("could do sth before func invoke")
        result = func(*args, **kwargs)
        return add_title(result)
    return wrapper


@aspect_decorator
def ret_name(name):
    return "Hello, %s!" % name


if __name__ == "__main__":
    now()
    
    wrapper_now()

    wrapper_args("good")

    print(ret_name("Student"))
