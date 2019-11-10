from ..geometric_mean import geometric_mean
from .formation import Formation
from ..units.solider import Solider


class Squad(Formation):
    def __init__(self, units: list) -> None:
        super().__init__(units)

    @property
    def attack_success(self) -> float:
        return geometric_mean([unit.attack_success
                               for unit in self.active_subformations])

    @property
    def charged_units(self) -> list:
        return [unit for unit in self.active_subformations if unit.is_charged]

    @property
    def charged_units_count(self) -> int:
        return len(self.charged_units)

    @property
    def damage(self) -> float:
        return sum(subformation.damage for subformation in self.charged_units)

    @property
    def total_damage(self) -> float:
        return sum(subformation.damage
                   for subformation in self.active_subformations)

    @property
    def power(self) -> float:
        return self.is_active * self.total_damage

    def get_damage(self, damage: float) -> None:
        damage_per_unit = damage / len(self.active_subformations)
        for unit in self.active_subformations:
            unit.get_damage(damage_per_unit)

    def attack(self, enemy_squad: object) -> None:
        if self.attack_success <= enemy_squad.attack_success:
            print('Attack failed!')
            return
        damage = self.damage
        charged_units = self.charged_units
        enemy_squad.get_damage(damage)
        print(f'\tSquad is attacking enemy squad. '
              f'Inflicted damage: {round(damage, 2)}')
        for unit in charged_units:
            unit.do_recharge()
            if isinstance(unit, Solider):
                unit.experience_gain()
