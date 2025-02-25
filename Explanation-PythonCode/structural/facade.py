class CPU:
    def start(self):
        print("CPU: Starting")

    def execute(self):
        print("CPU: Executing")

    def load(self):
        print("CPU: Loading data")

class Memory:
    def load(self, position, data):
        print(f"Memory: Loading {data} at {position}")

class HardDrive:
    def read(self, lba, size):
        print(f"HardDrive: Reading {size} from {lba}")

# Client code (complex interaction)
cpu = CPU()
memory = Memory()
hard_drive = HardDrive()

cpu.start()
memory.load(0, hard_drive.read(10, 5))
cpu.execute()


#With DEsign Pattern
class CPU:
    def start(self):
        print("CPU: Starting")

    def execute(self):
        print("CPU: Executing")

    def load(self):
        print("CPU: Loading data")

class Memory:
    def load(self, position, data):
        print(f"Memory: Loading {data} at {position}")

class HardDrive:
    def read(self, lba, size):
        print(f"HardDrive: Reading {size} from {lba}")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.start()
        data = self.hard_drive.read(10, 5)
        self.memory.load(0, data)
        self.cpu.execute()

# Client code (simplified interaction)
computer = ComputerFacade()
computer.start_computer()