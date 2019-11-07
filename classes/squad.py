from .geometric_mean import geometric_mean
from .army import Army
from .strategy import Strategy

class Squad:
    def __init__(self, units: list) -> None:
        self.units = units

    @property
    def active_units(self) -> list:
        return [unit for unit in self.units if unit.is_active]

    @property
    def is_active(self) -> bool:
        return any(unit.is_active for unit in self.units)

    @property
    def attack_success(self) -> float:
        return geometric_mean([unit.attack_success 
                for unit in self.active_units])
    
    @property
    def damage(self) -> float:
        return sum(unit.damage for unit in self.active_units)

    def get_damage(self, damage: float) -> None:
        damage_per_unit = damage / len(self.active_units)
        for unit in self.active_units:
            unit.get_damage(damage_per_unit)

    @property
    def power(self) -> float:
        return self.is_active * self.damage

    def attack(self, enemy: Army, strategy: Strategy):
        enemy_squad = strategy.choose(enemy) # TODO: допилить метод attack