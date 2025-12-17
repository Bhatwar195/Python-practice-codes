# Instance, Class and Static methods

class Demo:

    def instance_method(self):
        print("This is instance method")

    @classmethod
    def class_method(cls):
        print("This is class method")

    @staticmethod
    def static_method():
        print("This is static method")

d = Demo()
d.instance_method()
Demo.class_method()
Demo.static_method()
