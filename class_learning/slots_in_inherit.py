"""
    This will show how to restrict attr of instance
    Only attr in __slot__ can instance has, If subClass has __slots__, 
    it will inherit __slots__ from Parent. or Parent's __slots__ has no effect on 
    the child attr.
    
    Author: xiangtian.hu
    Date: 2017-6-9
"""


class Parent:
    """instance of Parent attr in __slots__"""
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Parent):
    pass


class Child2(Parent):
    __slots__ = tuple()
    pass

if __name__ == "__main__":
    child = Child("Child", 10)
    child.salary = 0  # Parent's slot will not affect child's attribute if Child has no __slot__

    child2 = Child2("Child2", 2)
    child2.salary = 0  # Parent's slot will affect child's attribute, this will cause error

    parent = Parent("Parent", 30)
    parent.salary = 10000  # add salary to Parent instance will cause error


