class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

# Deserialize
book_instance = Book.from_json(json_data.json)
print(book_instance.title, book_instance.author)
