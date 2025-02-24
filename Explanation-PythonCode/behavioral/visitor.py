# Visitor Design Pattern

# Without Design Pattern
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side

circle = Circle(5)
square = Square(4)

print(f"Circle Area: {circle.get_area()}, Perimeter: {circle.get_perimeter()}")
print(f"Square Area: {square.get_area()}, Perimeter: {square.get_perimeter()}")

# With Design Pattern
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def accept(self, visitor):
        visitor.visit_square(self)

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_square(self, square):
        pass

class AreaVisitor(Visitor):
    def visit_circle(self, circle):
        print(f"Circle Area: {3.14 * circle.radius * circle.radius}")

    def visit_square(self, square):
        print(f"Square Area: {square.side * square.side}")

class PerimeterVisitor(Visitor):
    def visit_circle(self, circle):
        print(f"Circle Perimeter: {2 * 3.14 * circle.radius}")

    def visit_square(self, square):
        print(f"Square Perimeter: {4 * square.side}")

circle = Circle(5)
square = Square(4)

area_visitor = AreaVisitor()
perimeter_visitor = PerimeterVisitor()

circle.accept(area_visitor)
square.accept(area_visitor)

circle.accept(perimeter_visitor)
square.accept(perimeter_visitor)