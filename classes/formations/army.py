from .formation import Formation
from ..strategy import STRATEGIES


class Army(Formation):
    def __init__(self, squads: list, strategy: str, name: str) -> None:
        super().__init__(squads)
        self.strategy = strategy
        self.name = name

    def attack(self, enemy: object) -> None:
        if not self.subformations.is_active:
            print(f"{self.name} cannot attack, because it has no active"
                  f" units")
            return
        squad = max(self.active_subformations,
                    key=lambda squad: squad.charged_units_count)
        if not squad.charged_units_count:
            print(f"{self.name} cannot attack, because it has no charged"
                  f" units.")
            return
        print(f"{self.name} is attacking {enemy.name}:")
        squad.attack(STRATEGIES[self.strategy]
                     .choose(enemy.active_subformations))
