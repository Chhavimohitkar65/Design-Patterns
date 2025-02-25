import sys
from pympler.asizeof import asizeof

# Without Flyweight Pattern
class Tree:
    def __init__(self, x, y, age, texture, color):
        self.x = x
        self.y = y
        self.age = age
        self.texture = texture
        self.color = color

    def display(self):
        print(f"Tree at ({self.x}, {self.y}), Age: {self.age}, Texture: {self.texture}, Color: {self.color}")

# Creating many individual trees
trees = [Tree(i, i, i % 10, "Rough", "Green") for i in range(100000)]

# Print memory usage
print(f"Memory usage without Flyweight: {asizeof(trees)} bytes")

# Display a few trees
for tree in trees[:5]:
    tree.display()

print("\n" + "-" * 50 + "\n")

# With Flyweight Pattern
class TreeType:
    def __init__(self, texture, color):
        self.texture = texture
        self.color = color

    def display(self):
        print(f"Texture: {self.texture}, Color: {self.color}")

class TreeFlyweight:
    def __init__(self, x, y, age, tree_type: TreeType):
        self.x = x
        self.y = y
        self.age = age
        self.tree_type = tree_type

    def display(self):
        print(f"Tree at ({self.x}, {self.y}), Age: {self.age}, ", end="")
        self.tree_type.display()

class TreeFactory:
    _tree_types = {}

    @staticmethod
    def get_tree_type(texture, color):
        key = (texture, color)
        if key not in TreeFactory._tree_types:
            TreeFactory._tree_types[key] = TreeType(texture, color)
        return TreeFactory._tree_types[key]

# Using Flyweight objects
tree_type = TreeFactory.get_tree_type("Rough", "Green")
trees_flyweight = [TreeFlyweight(i, i, i % 10, tree_type) for i in range(100000)]

# Print memory usage
print(f"Memory usage with Flyweight: {asizeof(trees_flyweight) + asizeof(TreeFactory._tree_types)} bytes")
print(f"Number of tree types: {len(TreeFactory._tree_types)}")

# Display a few trees
for tree in trees_flyweight[:5]:
    tree.display()