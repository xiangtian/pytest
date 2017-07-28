class Foo:
    def __init__(self, *args, **kwargs):
        print("__init__ %s" % self.__class__)

    def __new__(cls, *args, **kwargs):
        print("__new__%s" % cls)
        return object.__new__(cls, *args, **kwargs)


class Bar(Foo):
    def __new__(cls, *args, **kwargs):
        print("Bar.__new__%s" % cls)
        return object.__new__(cls, *args, **kwargs)


class Student(Foo):
    pass


class Male(Foo):
    def __init__(self, *args, **kwargs):
        print("Male.__init__ %s" % self.__class__)


class Female(Foo):
    def __init__(self, *args, **kwargs):
        print("Female.__init__ %s" % self.__class__)

    def __new__(cls, *args, **kwargs):
        print("__new__%s" % cls)
        return object.__new__(Foo, *args, **kwargs)


bar = Bar()  # Using Bar.__new__()
student = Student()  # Using Foo.__new__()
male = Male()   # Using Male.__init__()
female = Female()  # Female.__init__ will not be call, and Foo.__init__ will not be call either.
