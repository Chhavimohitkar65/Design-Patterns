# Without Design Pattern
class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_numbers(self):
        return self.numbers

numbers = NumberList([1, 2, 3, 4, 5])
for num in numbers.get_numbers():
    print(num)

# With Design Pattern
from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class NumberListIterator(Iterator):
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def next(self):
        if self.has_next():
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            return None

    def has_next(self):
        return self.index < len(self.numbers)

class NumberListAggregate(Aggregate):
    def __init__(self, numbers):
        self.numbers = numbers

    def create_iterator(self):
        return NumberListIterator(self.numbers)

numbers_aggregate = NumberListAggregate([1, 2, 3, 4, 5])
iterator = numbers_aggregate.create_iterator()
while iterator.has_next():
    print(iterator.next())