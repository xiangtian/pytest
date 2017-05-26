class Student(object):
    count = 0
    books = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass


def class_attr():
    """All instance share the class attribute"""
    print("--Class attribute operation--")
    Student.books.extend(["python","javascript"])
    print("Student book list: %s" %Student.books)
    
    # Class can add class attribute after class definition
    Student.hobbies = ["reading", "jogging", "swimming"]
    print("Student hobby list: %s" % Student.hobbies)
    print(dir(Student))
    print 


def special_class_attr():
    """
    Class special attribute
    :return: 
    """
    print("--Special Class attribute--")
    print(Student.__name__)
    print(Student.__doc__)
    print(Student.__bases__)
    print(Student.__dict__)
    # print Student.__mouble__
    print(Student.__class__)
    print


def instance_attr():
    print("--Instance attribute operation--")
    wilber = Student("Wilber", 28)
    print("%s is %d years old" %(wilber.name, wilber.age))

    # Instance can add instance attribute after instance created
    # "gender" attibute only belong to wilber
    wilber.gender = "male"
    print("%s is %s" %(wilber.name, wilber.gender))
    print(dir(wilber))

    # Instance can access class attribute
    wilber.books.append("C#")
    print(wilber.books)
    print()

    jim = Student("Jim", 26)
    print("%s is %d years old" %(jim.name, jim.age))
    # will share the same class attributes
    # will don't have the 'gender' attribute
    print(dir(jim))
    print(jim.books)
    print()


if __name__ == "__main__":
    class_attr()
    special_class_attr()
    instance_attr()
