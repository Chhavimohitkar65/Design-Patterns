# Observer Design Pattern

# Without Design Pattern
class Subject:
    def __init__(self):
        self.observers = []
        self.state = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_state(self, state):
        self.state = state
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.state)

class Observer:
    def update(self, state):
        print(f"Observer received state: {state}")

subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.set_state("New State")

# With Design Pattern
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self.observers = []
        self.state = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.state)

    def set_state(self, state):
        self.state = state
        self.notify_observers()

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(f"{self.name} received state: {state}")

subject = ConcreteSubject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.set_state("Updated State")