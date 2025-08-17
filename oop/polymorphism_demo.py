# polymorphism_demo.py
import math

class Shape:
    """
    Base class representing a generic Shape.
    """
    def area(self):
        """
        Method to calculate the area of the shape.
        Must be overridden in derived classes.
        """
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """
    Rectangle shape class inheriting from Shape.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        Formula: length × width
        """
        return self.length * self.width


class Circle(Shape):
    """
    Circle shape class inheriting from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        Formula: π × radius²
        """
        return math.pi * (self.radius ** 2)
