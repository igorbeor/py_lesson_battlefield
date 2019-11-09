from random import choice
from operator import attrgetter

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
    def choose(self, targets: list):
        return choice(targets)

class Weekest(Strategy):
    def choose(self, targets: list):
        return max(targets, key=attrgetter('power'))

class Strongest(Strategy):
    def choose(self, targets: list):
        return min(targets, key=attrgetter('power'))