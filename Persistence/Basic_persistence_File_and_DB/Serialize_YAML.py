import yaml

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Camry")

# Serialize
yaml_data = yaml.dump(car.__dict__)
print(yaml_data)

# Save to file
with open("car.yaml", "w") as file:
    yaml.dump(car.__dict__, file)
