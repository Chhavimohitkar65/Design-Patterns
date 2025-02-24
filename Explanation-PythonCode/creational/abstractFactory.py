class WindowsButton:
    def render(self):
        print("Rendering Windows Button")

class MacButton:
    def render(self):
        print("Rendering Mac Button")

class WindowsMenu:
    def render(self):
        print("Rendering Windows Menu")

class MacMenu:
    def render(self):
        print("Rendering Mac Menu")

def ui_manager(os_type):
    if os_type == "windows":
        button = WindowsButton()
        menu = WindowsMenu()
    elif os_type == "mac":
        button = MacButton()
        menu = MacMenu()
    else:
        print("Unknown OS type")
        return

    button.render()
    menu.render()


# Client code
ui_manager("windows") 
ui_manager("mac")  


#With Design Pattern
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Menu(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        print("Rendering Windows Button")

class MacButton(Button):
    def render(self):
        print("Rendering Mac Button")

class WindowsMenu(Menu):
    def render(self):
        print("Rendering Windows Menu")

class MacMenu(Menu):
    def render(self):
        print("Rendering Mac Menu")


class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_menu(self) -> Menu:
        pass

class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_menu(self) -> Menu:
        return WindowsMenu()


class MacUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_menu(self) -> Menu:
        return MacMenu()


def ui_manager(factory: UIFactory):
    button = factory.create_button()
    menu = factory.create_menu()

    button.render()
    menu.render()


windows_factory = WindowsUIFactory()
mac_factory = MacUIFactory()

ui_manager(windows_factory)
ui_manager(mac_factory)  