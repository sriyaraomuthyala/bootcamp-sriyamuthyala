def validate_args(func):
    def wrapper(*args, **kwargs):
        if any(arg is None for arg in args):
            raise ValueError("Invalid argument provided")
        return func(*args, **kwargs)
    return wrapper
