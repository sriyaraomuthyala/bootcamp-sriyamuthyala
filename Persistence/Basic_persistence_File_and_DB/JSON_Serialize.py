import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_json(self):
        return json.dumps(self.__dict__)

book = Book("1984", "George Orwell")
json_data = book.to_json()
print(json_data)
