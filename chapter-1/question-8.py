# Write a class Person that has a member function hello()


class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello, my name is", self.name)
        
        
p = Person('Matti')
p.hello()