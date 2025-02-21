import json
class MyCollection:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def to_json(self):
        return json.dumps([item.to_json() for item in self.items])

collection = MyCollection()
collection.add(Book("Brave New World", "Aldous Huxley"))
print(collection.to_json())
