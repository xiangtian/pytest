"""
    The instance attribute will overwrite class attribute
"""


class Student:
    count = 0
    grade = 2

    def __init__(self):
        self.count = 3

    def fun(self):
        self.grade = 5

if __name__ == "__main__":
    print(Student.__dict__)
    print(Student.count)
    s = Student()
    print("Instance attr:%s" % s.count)
    print(s.__dict__)
    print("Class attr:%s" % Student.count)
    print(Student.__dict__)

    print("Using instance method modify instance attr")
    Student.fun(s)
    print(s.grade)
    print(s.__dict__)
    print(Student.__dict__)
