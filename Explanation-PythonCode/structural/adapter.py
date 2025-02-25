class OldPrinter:
    def print_text(self, text):
        print(f"Old Printer: {text}")

class NewPrinter:
    def display_text(self, text):
        print(f"New Printer: {text}")

def client_code(printer):
    # This code expects a method named 'print_text'
    printer.print_text("Hello, World!")

old_printer = OldPrinter()
client_code(old_printer)  # Works fine

new_printer = NewPrinter()
#client_code(new_printer)  # This would cause an error


#With Design Pattern
class OldPrinter:
    def print_text(self, text):
        print(f"Old Printer: {text}")

class NewPrinter:
    def display_text(self, text):
        print(f"New Printer: {text}")

class NewPrinterAdapter:
    def __init__(self, new_printer):
        self.new_printer = new_printer

    def print_text(self, text):
        self.new_printer.display_text(text)

def client_code(printer):
    printer.print_text("Hello, World!")

old_printer = OldPrinter()
client_code(old_printer)  # Works fine

new_printer = NewPrinter()
new_printer_adapter = NewPrinterAdapter(new_printer)
client_code(new_printer_adapter)  # Works with the adapter