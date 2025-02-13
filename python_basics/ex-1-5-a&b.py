from config_loader import load_config

def say_hello(name: str) -> str:
    config = load_config()
    return " ".join([f"Hello, {name}!" for _ in range(config["num_times"])])
