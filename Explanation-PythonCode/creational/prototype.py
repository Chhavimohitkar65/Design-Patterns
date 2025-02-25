import copy
import time

class ComplexObject:
    def __init__(self, data):
        self.data = data
        time.sleep(5)
        print("Complex object initialized with:", self.data)

    def __str__(self):
        return f"ComplexObject(data={self.data})"

# Client code (creating objects repeatedly)
obj1 = ComplexObject({"key1": "value1", "key2": "value2"})
print(obj1)
obj2 = ComplexObject({"key1": "value1", "key2": "value2"})
print(obj2)
obj3 = ComplexObject({"key1": "value1", "key2": "value2"})
print(obj3)

#With Design Pattern
import copy
import time

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ComplexObject(Prototype):
    def __init__(self, data):
        self.data = data
        time.sleep(5)
        print("Complex object initialized with:", self.data)

    def __str__(self):
        return f"ComplexObject(data={self.data})"

# Client code (cloning the prototype)
prototype = ComplexObject({"key1": "value1", "key2": "value2"})

obj1 = prototype.clone()
print(obj1)
obj2 = prototype.clone()
print(obj2)
obj3 = prototype.clone()
print(obj3)