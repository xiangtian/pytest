"""
    How to call super.__init__ and call super_class's method
    Author: xiangtian.hu
    Date: 2017-6-9
"""


class Parent:
    numList = []

    def __init__(self, name):
        self.name = name

    def foo(self):
        print("This is from Parent.")


class Child(Parent):

    def __init__(self):
        super(Child, self).__init__("Parent")  # How to call super __init__
        self.sub_name = "Child"

    def foo(self):
        super(Child, self).foo()  # call Parent.foo in Child
        print("This is from Child")


class Child2(Parent):
    """
    Child2 does't has __init__()
    """
    pass

if __name__ == "__main__":
    print(issubclass(Child, Parent))
    child = Child()
    print(child.name)
    print(child.sub_name)

    child.foo()

    # Child2 does't def __init__, create subClass instance need using Parent __init__
    child2 = Child2("Child2")
    print(child2.name)

