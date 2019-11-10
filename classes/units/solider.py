from ..rand import Rand
from .unit import Unit


class Solider(Unit):

    def __init__(self, health: float = 100,
                 recharge: int = 500, experience: int = 0):
        super().__init__(health, recharge)
        self.experience = experience

    @property
    def experience(self) -> int:
        return self._experience

    @experience.setter
    def experience(self, value: int) -> None:
        if not 0 <= value <= 50:
            raise ValueError('experience value must be in range 0-50')
        self._experience = value

    @property
    def attack_success(self) -> float:
        return .5 * (1 + self.health/100) \
            * Rand.randint(50 + self.experience, 100) / 100

    @property
    def damage(self) -> float:
        return .05 + self.experience / 100

    @property
    def is_active(self) -> bool:
        return bool(self.health)

    def get_damage(self, damage: float) -> None:
        self.health = max(0, self.health - damage)

    def experience_gain(self) -> None:
        self.experience = min(self.experience + 1, 50)
