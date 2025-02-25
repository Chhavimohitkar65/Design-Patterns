class Coffee:
    def get_cost(self):
        return 5

    def get_description(self):
        return "Coffee"

class MilkCoffee(Coffee):
    def get_cost(self):
        return super().get_cost() + 2

    def get_description(self):
        return super().get_description() + ", Milk"

class SugarCoffee(Coffee):
    def get_cost(self):
        return super().get_cost() + 1

    def get_description(self):
        return super().get_description() + ", Sugar"

class MilkSugarCoffee(Coffee):
    def get_cost(self):
        return super().get_cost() + 3

    def get_description(self):
        return super().get_description() + ", Milk, Sugar"

# Client code
coffee = MilkSugarCoffee()
print(f"{coffee.get_description()} - Cost: ${coffee.get_cost()}")


#With Design Pattern
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

class SimpleCoffee(Coffee):
    def get_cost(self):
        return 5

    def get_description(self):
        return "Coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost()

    def get_description(self):
        return self.coffee.get_description()

class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return super().get_cost() + 2

    def get_description(self):
        return super().get_description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def get_cost(self):
        return super().get_cost() + 1

    def get_description(self):
        return super().get_description() + ", Sugar"

# Client code
coffee = SimpleCoffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(f"{coffee.get_description()} - Cost: ${coffee.get_cost()}")

coffee2 = SimpleCoffee()
coffee2 = MilkDecorator(coffee2)
print(f"{coffee2.get_description()} - Cost: ${coffee2.get_cost()}")