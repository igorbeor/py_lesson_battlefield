from .rand import Rand
from operator import attrgetter


STRATEGIES = {}


def register_class(target_class):
    STRATEGIES[target_class.__name__] = target_class


class MetaRegistry(type):

    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        if name not in STRATEGIES:
            register_class(cls)
        return cls


class Random(metaclass=MetaRegistry):
    @classmethod
    def choose(cls, targets: list) -> object:
        return Rand.choice(targets)


class Weekest(metaclass=MetaRegistry):
    @classmethod
    def choose(cls, targets: list) -> object:
        return max(targets, key=attrgetter('power'))


class Strongest(metaclass=MetaRegistry):
    @classmethod
    def choose(cls, targets: list) -> object:
        return min(targets, key=attrgetter('power'))
