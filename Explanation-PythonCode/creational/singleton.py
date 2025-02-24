class Configuration:
    def __init__(self):
        self.settings = {"debug": True, "log_level": "INFO"}

    def get_setting(self, key):
        return self.settings.get(key)

config1 = Configuration()
config2 = Configuration()

print(config1.get_setting("debug"))
print(config2.get_setting("log_level"))

print(config1 is config2)

#With Design Pattern
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Configuration(metaclass=Singleton):
    def __init__(self):
        self.settings = {"debug": True, "log_level": "INFO"}

    def get_setting(self, key):
        return self.settings.get(key)

config1 = Configuration()
config2 = Configuration()

print(config1.get_setting("debug"))  
print(config2.get_setting("log_level"))  

print(config1 is config2)