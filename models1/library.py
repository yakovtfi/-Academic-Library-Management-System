from models1.user import User
from models1.book import Book
from models1.logger import Logger
from models1.systemAdmin import SystemAdmin

class Library:
    max_borrow_days: int = 14

    def __init__(self):
        self.books: dict[str, Book] = {}
        self.users: dict[str, User] = {}

    def register_user(self, user: User) -> None:
        self.users[user.user_id] = user
        Logger.log_action("REGISTER_USER", f"{user.name} ({user.user_id}) added to library.")

    def add_book(self, book: Book) -> None:
        self.books[book.isbn] = book
        Logger.log_action("ADD_BOOK", f"Added book '{book.title}' ({book.isbn}).")

    def perform_borrow(self, user_id: str, isbn: str) -> None:
        assert user_id in self.users, "User not found!"
        assert isbn in self.books, "Book not found!"
        user = self.users[user_id]
        book = self.books[isbn]
        if not book.is_available:
            raise Exception("Book is already borrowed!")
        user.borrow_book(book)
        book.is_available = False
        Logger.log_action("BORROW", f"User {user.name} borrowed '{book.title}'.")
        SystemAdmin.update_transactions_count()

    def perform_return(self, user_id: str, isbn: str) -> None:
        assert user_id in self.users, "User not found!"
        assert isbn in self.books, "Book not found!"
        user = self.users[user_id]
        book = self.books[isbn]
        if book.is_available:
            raise Exception("Book is already available!")
        if book not in user.borrowed_books:
            raise Exception("This user did not borrow this book!")
        user.return_book(book)
        book.is_available = True
        Logger.log_action("RETURN", f"User {user.name} returned '{book.title}'.")
        SystemAdmin.update_transactions_count()