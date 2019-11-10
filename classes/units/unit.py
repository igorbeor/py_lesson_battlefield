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
        if not 0 <= value <= 100:
            raise ValueError('health value must be in range 0-100')
        self._health = value

    @property
    def recharge(self) -> int:
        return self._recharge

    @recharge.setter
    def recharge(self, value: int) -> None:
        if not 100 <= value <= 2000:
            raise ValueError('recharge value must be in range 100-2000')
        self._recharge = value

    def do_recharge(self) -> None:
        self.recharge_timer = round(monotonic() * 1000) + self.recharge

    @property
    def is_charged(self) -> bool:
        return self.recharge_timer < round(monotonic() * 1000)
