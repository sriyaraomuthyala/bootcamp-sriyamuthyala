import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class Data(JsonMixin):
    def __init__(self, value):
        self.value = value