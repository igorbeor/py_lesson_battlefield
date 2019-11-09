class Formation:
    def __init__(self, subformations: list) -> None:
        self.subformations = subformations

    @property
    def is_active(self) -> bool:
        return any(subformation.is_active for subformation in self.subformations)

    @property
    def active_subformations(self) -> list:
        return [subformation for subformation in self.subformations if subformation.is_active]
    
    @property
    def damage(self) -> float:
        return sum(subformation.damage for subformation in self.active_subformations)

    @property
    def power(self) -> float:
        return self.is_active * self.damage
