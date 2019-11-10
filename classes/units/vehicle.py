from ..rand import Rand
from .unit import Unit
from ..geometric_mean import geometric_mean


class Vehicle(Unit):

    def __init__(self, operators: list, health: float = 200,
                 recharge: int = 2000) -> None:
        super().__init__(health, recharge)
        self.operators = operators

    @property
    def operators(self) -> list:
        return self._operators

    @operators.setter
    def operators(self, value: list) -> None:
        if not isinstance(value, list):
            raise ValueError('operators must be list')
        if not 1 <= len(value) <= 3:
            raise ValueError('operators count must be in range 1-3')
        self._operators = value

    @property
    def total_health(self) -> float:
        return sum(operator.health for operator in self.active_operators) \
            / len(self.active_operators) + self.health

    @property
    def attack_success(self) -> float:
        return .5 * (1 + self.health / 100) * \
            geometric_mean([operator.attack_success
                            for operator in self.active_operators])

    @property
    def damage(self) -> float:
        return .1 + sum(operator.experience / 100
                        for operator in self.active_operators)

    @property
    def is_active(self) -> bool:
        return bool(self.health) and bool(self.active_operators)

    @property
    def active_operators(self) -> list:
        return [operator for operator in self.operators
                if operator.is_active]

    def get_damage(self, damage: float) -> None:
        self.health = max(0, self.health - damage * .6)

        if self.health == 0:
            for operator in self.active_operators:
                operator.health = 0

        if len(self.active_operators) > 1:
            loser = Rand.choice(self.active_operators)
            loser.get_damage(damage * .2)
            other_operator_damage = damage * .2 \
                / (len(self.active_operators) - 1)
            for operator in self.active_operators:
                if operator is not loser:
                    operator.get_damage(other_operator_damage)
        else:
            operator = self.active_operators[0]
            operator.get_damage(damage * .4)
