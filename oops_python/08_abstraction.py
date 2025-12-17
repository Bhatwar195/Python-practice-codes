# Abstraction using abstract class

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of square =", 4 * 4)

s = Square()
s.area()
