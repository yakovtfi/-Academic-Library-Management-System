class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def get_details(self) -> str:
        status = "Available" if self.is_available else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"