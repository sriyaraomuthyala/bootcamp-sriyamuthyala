class Book:
    book_count = 0
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.book_count += 1
    
    @staticmethod
    def validate_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()
    
    @classmethod
    def total_books(cls):
        return cls.book_count
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
    def __repr__(self):
        return self.__str__()