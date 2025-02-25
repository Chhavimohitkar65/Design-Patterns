class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalSound:
    def __init__(self, animal_type):
        if animal_type == "dog":
            self.animal = Dog()
        elif animal_type == "cat":
            self.animal = Cat()
        else:
            raise ValueError("Unknown animal type")
    
    def make_sound(self):
        return self.animal.speak()

# Client code
animal_sound = AnimalSound("dog")
print(animal_sound.make_sound())

#With Design Pattern

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

class AnimalSound:
    def __init__(self, factory: AnimalFactory):
        self.animal = factory.create_animal()
    
    def make_sound(self):
        return self.animal.speak()

# Client code
dog_factory = DogFactory()
animal_sound = AnimalSound(dog_factory)
print(animal_sound.make_sound())  # Output: Woof!

cat_factory = CatFactory()
animal_sound = AnimalSound(cat_factory)
print(animal_sound.make_sound())  # Output: Meow!