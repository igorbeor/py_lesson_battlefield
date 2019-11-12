from time import monotonic


class Unit:

    def __init__(self, health: float, recharge: int) -> None:
        self.health = health
        self.recharge = recharge
        self.recharge_timer = 0

    @property
    def health(self) -> float:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(min(value, 100), 0)

    @property
    def recharge(self) -> int:
        return self._recharge

    @recharge.setter
    def recharge(self, value: int) -> None:
        self._recharge = max(min(value, 2000), 100)

    def do_recharge(self) -> None:
        self.recharge_timer = round(monotonic() * 1000) + self.recharge / 100

    @property
    def is_charged(self) -> bool:
        return self.recharge_timer < round(monotonic() * 1000)
