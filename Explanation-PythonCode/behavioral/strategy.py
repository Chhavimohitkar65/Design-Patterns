# Without Design Pattern
class Context:
    def __init__(self, strategy_type):
        self.strategy_type = strategy_type

    def execute_strategy(self, data):
        if self.strategy_type == "strategy_a":
            print(f"Executing Strategy A with data: {data}")
        elif self.strategy_type == "strategy_b":
            print(f"Executing Strategy B with data: {data}")

context_a = Context("strategy_a")
context_b = Context("strategy_b")

context_a.execute_strategy("Data 1")
context_b.execute_strategy("Data 2")

# With Design Pattern
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print(f"Executing Strategy A with data: {data}")

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print(f"Executing Strategy B with data: {data}")

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        self.strategy.execute(data)

strategy_a = ConcreteStrategyA()
strategy_b = ConcreteStrategyB()

context_a = Context(strategy_a)
context_b = Context(strategy_b)

context_a.execute_strategy("Data 1")
context_b.execute_strategy("Data 2")