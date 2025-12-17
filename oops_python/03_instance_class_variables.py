# Instance variable vs Class variable

class Student:
    college = "PCE"

    def __init__(self, name):
        self.name = name

s1 = Student("Bhavesh")
s2 = Student("Pranay")

print(s1.name, s1.college)
print(s2.name, s2.college)
