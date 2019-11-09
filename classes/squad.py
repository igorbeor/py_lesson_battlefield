from .geometric_mean import geometric_mean
from .army import Army
from .strategy import Strategy
from .formation import Formation

class Squad(Formation):
    def __init__(self, units: list) -> None:
        super().__init__(units)

    @property
    def attack_success(self) -> float:
        return geometric_mean([unit.attack_success 
                for unit in self.active_subformations])
    
    def get_damage(self, damage: float) -> None:
        damage_per_unit = damage / len(self.active_subformations)
        for unit in self.active_subformations:
            unit.get_damage(damage_per_unit)

    def attack(self, enemy: Army, strategy: Strategy):
        enemy_squad = strategy.choose(enemy) # TODO: допилить метод attack