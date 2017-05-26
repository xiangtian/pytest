"""
    Usage of over_writen

"""


class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print ("woman")


class Child(Person):
    def print_title(self):
        if self.sex == "male":
            print("boy")
        elif self.sex == "female":
            print("girl")

person = Person("H", "male")
person.print_title()

child = Child("X", "male")
child.print_title()

