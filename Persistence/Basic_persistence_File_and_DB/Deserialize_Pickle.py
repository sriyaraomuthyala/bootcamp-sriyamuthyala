import pickle
with open("person.pkl", "rb") as file:
    loaded_person = pickle.load(file)

print(loaded_person.name, loaded_person.institutions, loaded_person.colleagues)
