import json
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # Sensitive data

    def to_json(self):
        return json.dumps({"username": self.username})  # Exclude password

user = User("john_doe", "secret123")
print(user.to_json())
