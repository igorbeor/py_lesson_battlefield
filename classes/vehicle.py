import math
from random import random, choice
from functools import reduce
from .unit import Unit
from .descriptors.operators import Operators

def gavg(xs):
    return math.exp(math.fsum(math.log(x) for x in xs) / len(xs))

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
        return .5 * (1 + self.health / 100) * \
            gavg([operator.attack_success for operator in self.operators])

    @property
    def damage(self):
        return .1 + \
            sum(operator.experience / 100 for operator in self.operators)

    @property
    def is_active(self):
        return self.health > 0 and \
            reduce(lambda a, b: a or b, [o.is_alive for o in self.operators])

    @property
    def active_operators(self):
        return [operator for operator in self.operators if operator.is_alive]

    def get_damage(self, damage):
        self.health = max(0, self.health - damage * .6)
        
        if len(self.operators) > 1:
            loser = choice(self.operators)
            loser.get_damage(damage * .2)
            other_operator_damage = damage * .2 / (len(self.operators) - 1)
            for operator in self.operators:
                if operator is not loser:
                    operator.get_damage(other_operator_damage)
        else:
            operator = self.operator[0]
            operator.get_damage(damage * .4)

        if self.health == 0:
            for operator in self.operators:
                operator.health = 0
