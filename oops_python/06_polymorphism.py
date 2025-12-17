# Polymorphism example

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
