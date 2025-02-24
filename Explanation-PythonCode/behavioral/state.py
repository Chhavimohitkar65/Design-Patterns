# State Design Pattern

# Without Design Pattern
class Context:
    def __init__(self):
        self.state = "State A"

    def request(self):
        if self.state == "State A":
            print("Handling request in State A")
            self.state = "State B"
        elif self.state == "State B":
            print("Handling request in State B")
            self.state = "State A"

context = Context()
context.request()
context.request()

# With Design Pattern
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        print("Handling request in State A")
        context.set_state(ConcreteStateB())

class ConcreteStateB(State):
    def handle(self, context):
        print("Handling request in State B")
        context.set_state(ConcreteStateA())

class Context:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)

stateA = ConcreteStateA()
context = Context(stateA)

context.request()
context.request()