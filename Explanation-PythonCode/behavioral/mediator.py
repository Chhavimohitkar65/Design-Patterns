# Mediator Design Pattern

# Without Design Pattern
class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, message, receiver):
        print(f"{self.name} sends message '{message}' to {receiver.name}")

user1 = User("Alice")
user2 = User("Bob")

user1.send_message("Hello Bob!", user2)
user2.send_message("Hi Alice!", user1)

# With Design Pattern
from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send_message(self, message, sender):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive_message(message, sender)

class User(ABC):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_message(self, message, sender):
        pass

class ConcreteUser(User):
    def send_message(self, message):
        self.mediator.send_message(message, self)

    def receive_message(self, message, sender):
        print(f"{self.name} receives message '{message}' from {sender.name}")

mediator = ConcreteMediator()
alice = ConcreteUser("Alice", mediator)
bob = ConcreteUser("Bob", mediator)

mediator.add_user(alice)
mediator.add_user(bob)

alice.send_message("Hello Bob!")
bob.send_message("Hi Alice!")