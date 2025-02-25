class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class Box:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total_price(self):
        total = 0
        for item in self.items:
            if isinstance(item, Product):
                total += item.get_price()
            elif isinstance(item, Box):
                total += item.get_total_price()
        return total

# Client Code
product1 = Product("Laptop", 1200)
product2 = Product("Mouse", 25)
box1 = Box()
box1.add_item(product1)
box1.add_item(product2)

print(f"Box 1 Total Price: ${box1.get_total_price()}")

product3 = Product("Keyboard", 50)
box2 = Box()
box2.add_item(product3)
box2.add_item(box1)

print(f"Box 2 Total Price: ${box2.get_total_price()}")


#With Design Pattern
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def get_price(self):
        pass

class Product(Component):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class Box(Component):
    def __init__(self):
        self.items = []

    def add_item(self, item: Component):
        self.items.append(item)

    def get_price(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

# Client Code
product1 = Product("Laptop", 1200)
product2 = Product("Mouse", 25)
box1 = Box()
box1.add_item(product1)
box1.add_item(product2)

print(f"Box 1 Total Price: ${box1.get_price()}")

product3 = Product("Keyboard", 50)
box2 = Box()
box2.add_item(product3)
box2.add_item(box1)

print(f"Box 2 Total Price: ${box2.get_price()}")

#add packaging cost.
class BoxWithPackaging(Component):
    def __init__(self, box, packaging_cost):
        self.box = box
        self.packaging_cost = packaging_cost

    def get_price(self):
        return self.box.get_price() + self.packaging_cost

box3 = BoxWithPackaging(box2, 10)
print(f"Box 3 Total Price with packaging: ${box3.get_price()}")