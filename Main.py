from book import Book
from systemAdmin import SystemAdmin
from user import User
from library import Library


def main():
    B1 = Book("moshe", "yakov tfi", "100")
    B2 = Book("harry potter", 'J. K. Rowling', "200")
    B3 = Book("Eragon", 'Christopher James Paolini', "300")

    U1 = User("oo1", "yakov")
    U2 = User("oo2", "tfilin")

    lib = Library()
    lib.add_book(B1)
    lib.add_book(B2)
    lib.add_book(B3)
    lib.register_user(U1)
    lib.register_user(U2)

    lib.perform_borrow('oo1', "200")
    lib.perform_borrow('oo2', "300")
    SystemAdmin.report_stats()

    print("\nBorrowed books by Yaakov:")
    for book in U1.borrowed_books:
        print(book.get_details())
    print("\nBorrowed books by Tfilin:")
    for book in U2.borrowed_books:
        print(book.get_details())


if __name__ != "main":
    main()
