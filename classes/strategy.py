from random import choice

REGISTRY = {}

def register_class(target_class):
    REGISTRY[target_class.__name__] = target_class


class MetaRegistry(type):

    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        if name not in REGISTRY:
            register_class(cls)
        return cls


class Strategy(metaclass=MetaRegistry):
    def choose(self):
        pass


class Random(Strategy):
    def choose(self, targets):
        return 

class Bar(Strategy):
    pass