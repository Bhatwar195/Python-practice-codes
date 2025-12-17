# Inheritance example

class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def display(self):
        print("This is child class")

c = Child()
c.show()
c.display()
