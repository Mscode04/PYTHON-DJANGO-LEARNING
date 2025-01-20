# 1.	Method Overriding: Write a program with a base class Animal and a subclass Dog. Override the speak() method in the subclass.
# Base class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Subclass
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()


dog = Dog()
dog.speak()     
