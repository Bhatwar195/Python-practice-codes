# Constructor (__init__)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Bhavesh", 19)
print(s1.name, s1.age)
