class Operators:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError('operators must be list')
        if not 1 <= len(value) <= 3:
            raise ValueError('operators count must be in range 1-3')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name