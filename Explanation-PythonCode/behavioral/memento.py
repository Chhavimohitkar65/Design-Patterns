# Without Design Pattern
class Document:
    def __init__(self, content):
        self.content = content

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

document = Document("Initial content")
document.set_content("Modified content")
print(document.get_content())

# With Design Pattern
class Memento:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content

class Originator:
    def __init__(self, content):
        self.content = content

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def save_to_memento(self):
        return Memento(self.content)

    def restore_from_memento(self, memento):
        self.content = memento.get_content()

class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]

originator = Originator("Initial content")
caretaker = Caretaker()

caretaker.add_memento(originator.save_to_memento())

originator.set_content("Modified content")
caretaker.add_memento(originator.save_to_memento())

print(originator.get_content())

originator.restore_from_memento(caretaker.get_memento(0))
print(originator.get_content())