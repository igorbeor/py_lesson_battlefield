from .formation import Formation

class Army(Formation):
    def __init__(self, squads: list) -> None:
        super().__init__(squads)
