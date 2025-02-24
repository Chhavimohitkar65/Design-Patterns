class RedCircle:
    def draw(self):
        print("Drawing a Red Circle")

class BlueCircle:
    def draw(self):
        print("Drawing a Blue Circle")

class RedSquare:
    def draw(self):
        print("Drawing a Red Square")

class BlueSquare:
    def draw(self):
        print("Drawing a Blue Square")

# Client Code
red_circle = RedCircle()
blue_square = BlueSquare()

red_circle.draw()
blue_square.draw()

# To add a green circle and green square, you would need to add
# GreenCircle and GreenSquare classes, increasing the class count exponentially.

#With Design Pattern
from abc import ABC, abstractmethod

# Implementation (Color Hierarchy)
class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

class Red(Color):
    def apply_color(self):
        return "Red"

class Blue(Color):
    def apply_color(self):
        return "Blue"

# Abstraction (Shape Hierarchy)
class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        color = self.color.apply_color()
        print(f"Drawing a {color} Circle")

class Square(Shape):
    def draw(self):
        color = self.color.apply_color()
        print(f"Drawing a {color} Square")

# Client Code
red_color = Red()
blue_color = Blue()

red_circle = Circle(red_color)
blue_square = Square(blue_color)

red_circle.draw()
blue_square.draw()

# Adding a new color without changing the shape hierarchy
class Green(Color):
    def apply_color(self):
        return "Green"

green_color = Green()
green_circle = Circle(green_color)
green_circle.draw()

# Adding a new shape without changing the color hierarchy
class Triangle(Shape):
    def draw(self):
        color = self.color.apply_color()
        print(f"Drawing a {color} Triangle")

red_triangle = Triangle(red_color)
red_triangle.draw()