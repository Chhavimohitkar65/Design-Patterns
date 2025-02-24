# Without Design Pattern
class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class Switch:
    def __init__(self, light):
        self.light = light

    def flip(self, command):
        if command == "ON":
            self.light.on()
        elif command == "OFF":
            self.light.off()

# Client code
light = Light()
switch = Switch(light)
switch.flip("ON")
switch.flip("OFF")

# With Design Pattern
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    def undo(self):
        pass  # Optional undo method

class Light:
    def __init__(self):
        self.is_on = False
        self.previous_state = False #added previous_state

    def turn_on(self):
        self.previous_state = self.is_on
        self.is_on = True
        print("Light turned on")

    def turn_off(self):
        self.previous_state = self.is_on
        self.is_on = False
        print("Light turned off")

class LightOnUndoCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        if self.light.previous_state:
            self.light.turn_on()
        else:
            self.light.turn_off()

class LightOffUndoCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        if self.light.previous_state:
            self.light.turn_on()
        else:
            self.light.turn_off()

class SwitchUndo:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()

    def undo(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].undo()

# Client code
light = Light()
light_on = LightOnUndoCommand(light)
light_off = LightOffUndoCommand(light)

switch_undo = SwitchUndo()
switch_undo.register("ON", light_on)
switch_undo.register("OFF", light_off)

switch_undo.execute("ON")
switch_undo.execute("OFF")

switch_undo.undo("OFF")
switch_undo.undo("ON")