def add_method(cls):
    cls.new_method = lambda self: "New method added!"
    return cls

@add_method
class DecoratedClass:
    pass