from .descriptors.health import Health
from .descriptors.recharge import Recharge

class Unit:

    health = Health()
    recharge = Recharge()

    def __init__(self, health, recharge):
        self.health = health
        self.recharge = recharge
