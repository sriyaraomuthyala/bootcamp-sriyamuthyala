import os
import yaml

def load_config():
    paths = ["./_config.yaml"] + os.getenv("CONFIG_PATH", "").split(":")
    for path in paths:
        if os.path.exists(path):
            with open(path, "r") as file:
                return yaml.safe_load(file)
    return {"num_times": 1} 