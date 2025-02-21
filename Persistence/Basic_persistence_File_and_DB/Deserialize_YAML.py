import yaml

# Define the Car class before deserializing
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Read YAML file
with open("car.yaml", "r") as file:
    car_data = yaml.safe_load(file)  # Convert YAML to dictionary

# Deserialize into a Car object
car_instance = Car(**car_data)

# Print the object properties
print(f"Brand: {car_instance.brand}, Model: {car_instance.model}")
