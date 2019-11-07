class Army:
    def __init__(self, squads) -> None:
        self.squads = squads

    @property
    def damage(self) -> float:
        return sum(squad.damage for squad in self.active_squads)
    
    @property
    def is_active(self) -> bool:
        return any(squad.is_active for squad in self.squads)

    @property
    def active_squads(self) -> list:
        return [squad for squad in self.squads if squad.is_active]

    @property
    def power(self) -> float:
        return self.is_active * self.damage