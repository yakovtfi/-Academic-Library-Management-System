from models1.book import Book

class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)