import json
class VersionedClass:
    def __init__(self, name, version=1):
        self.name = name
        self.version = version

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        if "version" not in data:
            data["version"] = 1  # Handle older versions
        return cls(**data)

old_json = '{"name": "Alice"}'  # Older version without version field
new_instance = VersionedClass.from_json(old_json)
print(new_instance.name, new_instance.version)
