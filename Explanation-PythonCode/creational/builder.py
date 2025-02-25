class Computer:
    def __init__(self, cpu, ram, storage, graphics_card, monitor, keyboard, mouse):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.graphics_card = graphics_card
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse

    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, Graphics={self.graphics_card}, Monitor={self.monitor}, Keyboard={self.keyboard}, Mouse={self.mouse}"

# Client code (very cumbersome)
computer = Computer("Intel i9", "32GB", "1TB SSD", "Nvidia RTX 3080", "4K Monitor", "Mechanical Keyboard", "Gaming Mouse")
print(computer)

#With Design Pattern
class Computer:
    def __init__(self, cpu, ram, storage, graphics_card, monitor, keyboard, mouse):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.graphics_card = graphics_card
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse

    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, Graphics={self.graphics_card}, Monitor={self.monitor}, Keyboard={self.keyboard}, Mouse={self.mouse}"

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphics_card = None
        self.monitor = None
        self.keyboard = None
        self.mouse = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def set_graphics_card(self, graphics_card):
        self.graphics_card = graphics_card
        return self

    def set_monitor(self, monitor):
        self.monitor = monitor
        return self

    def set_keyboard(self, keyboard):
        self.keyboard = keyboard
        return self

    def set_mouse(self, mouse):
        self.mouse = mouse
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage, self.graphics_card, self.monitor, self.keyboard, self.mouse)

# Client code (clean and readable)
builder = ComputerBuilder()
computer = builder.set_cpu("Intel i9").set_ram("32GB").set_storage("1TB SSD").set_graphics_card("Nvidia RTX 3080").set_monitor("4K Monitor").set_keyboard("Mechanical Keyboard").set_mouse("Gaming Mouse").build()
print(computer)

# Example with optional components
office_computer = ComputerBuilder().set_cpu("Intel i5").set_ram("16GB").set_storage("512GB SSD").set_keyboard("Standard Keyboard").set_mouse("Standard Mouse").build()
print(office_computer)