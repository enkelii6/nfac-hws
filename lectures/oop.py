class Parent:
    def method(self):
        print('Parent method')


class Child(Parent):
    def method(self):
        super().method()
        print('Child method')


c = Child()
c.method()
