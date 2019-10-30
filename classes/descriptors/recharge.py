class Recharge:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not 100 <= value <= 2000:
                raise ValueError('recharge value must be in range 100-2000')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name