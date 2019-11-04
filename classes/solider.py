from random import random
from .unit import Unit
from .descriptors.experience import Experience


class Solider(Unit):

    experience = Experience()

    def __init__(self, health, recharge, experience):
        super().__init__(health, recharge)
        self.experience = experience

    @property
    def atack(self):
        return .5 * (1 + self.health/100) * random(50 + self.experience, 100) / 100

    @property
    def damage(self):
        return .05 + self.experience / 100

    @property
    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health = max(0, self.health - damage)
