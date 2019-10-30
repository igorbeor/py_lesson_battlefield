class Experience:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not 0 <= value <= 50:
            raise ValueError('experience value must be in range 0-50')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name