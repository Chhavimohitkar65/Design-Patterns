class Request:
    def __init__(self, type, content):
        self.type = type
        self.content = content

def handle_request(request):
    if request.type == "type1":
        print(f"Handling type1 request: {request.content}")
    elif request.type == "type2":
        print(f"Handling type2 request: {request.content}")
    elif request.type == "type3":
        print(f"Handling type3 request: {request.content}")
    else:
        print(f"Unknown request type: {request.type}")

# Client code
request1 = Request("type1", "Content 1")
request2 = Request("type2", "Content 2")
request3 = Request("type3", "Content 3")
request4 = Request("type4", "Content 4")

handle_request(request1)
handle_request(request2)
handle_request(request3)
handle_request(request4)

#With Design Pattern
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

class Type1Handler(Handler):
    def handle_request(self, request):
        if request.type == "type1":
            print(f"Type1Handler: Handling request: {request.content}")
        elif self.successor:
            self.successor.handle_request(request)
        else:
            print(f"Type1Handler: No handler found for request: {request.type}")

class Type2Handler(Handler):
    def handle_request(self, request):
        if request.type == "type2":
            print(f"Type2Handler: Handling request: {request.content}")
        elif self.successor:
            self.successor.handle_request(request)
        else:
            print(f"Type2Handler: No handler found for request: {request.type}")

class Type3Handler(Handler):
    def handle_request(self, request):
        if request.type == "type3":
            print(f"Type3Handler: Handling request: {request.content}")
        elif self.successor:
            self.successor.handle_request(request)
        else:
            print(f"Type3Handler: No handler found for request: {request.type}")

class Request:
    def __init__(self, type, content):
        self.type = type
        self.content = content

# Client code
handler1 = Type1Handler()
handler2 = Type2Handler()
handler3 = Type3Handler()

handler1.successor = handler2
handler2.successor = handler3

request1 = Request("type1", "Content 1")
request2 = Request("type2", "Content 2")
request3 = Request("type3", "Content 3")
request4 = Request("type4", "Content 4")

handler1.handle_request(request1)
handler1.handle_request(request2)
handler1.handle_request(request3)
handler1.handle_request(request4)