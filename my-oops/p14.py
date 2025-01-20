from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass  

# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


circle = Circle(5)  
rectangle = Rectangle(4, 6)  

# Calculate and print areas
print(f"Area of Circle: {circle.calculate_area():.2f}")  
print(f"Area of Rectangle: {rectangle.calculate_area()}") 
