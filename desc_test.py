"""
   How to using Desc Class
"""
class Desc(object):
    """This is the Descriptor class,
       it has __get__, __set__, __delete__ function
    """
    def __get__(self, inst, type):
        print('get', self, inst, type)

    def __set__(self, inst, value):
        print('set', self, inst, value)


class Demo(object):
    desc = Desc()


class DemoInst(object):
    def __init__(self):
        self.desc = Desc()

# Only class property will call __get__ and __set__ method
demo = Demo()
print(demo)
demo.desc
demo.desc = 'my desc'
print("--------------")

# Instance property will't call __get__ and __set__method
demoInst = DemoInst()
print(demoInst)
demoInst.desc
demoInst.desc = "my desc"

print(demo.__dict__)
print("--------------")
print(demoInst.__dict__)
