def role_required(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role == role:
                return func(*args, **kwargs)
            else:
                print("Access denied")
        return wrapper
    return decorator