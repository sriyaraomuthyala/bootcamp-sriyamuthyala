import pickle

class Person:
    def __init__(self, name, institutions, colleagues):
        self.name = name
        self.institutions = institutions
        self.colleagues = colleagues

# Create an instance
person = Person("Alice", ["MIT", "Harvard"], ["Bob", "Charlie"])

# Serialize and save to file
with open("person.pkl", "wb") as file:
    pickle.dump(person, file)
