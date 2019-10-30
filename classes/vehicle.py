from random import random
from functools import reduce
from statistics import geometric_mean
from .unit import Unit
from .descriptors.operators import Operators


class Vehicle(Unit):

    operators = Operators()

    def __init__(self, health, recharge, operators):
        super().__init__(health, recharge)
        self.operators = operators

    @property
    def total_health(self):
        return sum(self.operators) // len(self.operators) + self.health

    @property
    def atack(self):
        return .5 * (1 + vehicle.health / 100) * gavg(operators.attack_success)

    # @property
    # def damage(self):
    #     return .05 + self.experience / 100

    @property
    def is_active(self):
        return self.health > 0 and \
            reduce(lambda a, b: a or b, [o.is_alive for o in self.operators])