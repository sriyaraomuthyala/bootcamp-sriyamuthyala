def custom_logger(log_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(log_message)
            result = func(*args, **kwargs)
            print("Execution finished")
            return result
        return wrapper
    return decorator