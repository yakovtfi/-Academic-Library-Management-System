class Books:
    def __init__(self,title=str,author=str,isbn=str,is_available=bool):
        self.title=title
        self.autho=author
        self.isbn=isbn
        self.is_available=is_available
    def get_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.is_available}")

class users:
    def __init__(self,name=str,user_id=int):
        self.name=name
        self.user_id=user_id
        self.borrowed_books=[]
    def borrow_book(self,book):
        if book.is_available:
            book.is_available=False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available")
    def return_book(self,book):
        if book in self.borrowed_books:
            book.is_available=True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")
class Library:
    def __init__(self):
        self.books_collection=[]
        self.users_list=[]
    def add_book(self,book):
        self.books_collection.append(book)
        print(f"Added book: {book.title}")
    def register_user(self,user):
        self.users_list.append(user)
        print(f"Registered user: {user.name}")
    def display_books(self):
        for book in self.books_collection:
            book.get_details()
    def display_users(self):
        for user in self.users_list:
            print(f"User Name: {user.name}, User ID: {user.user_id}, Borrowed Books: {[book.title for book in user.borrowed_books]}")
    def perform_borrow(self,user_id=str,book_isbn=str):
        user=None
        book=None
        for u in self.users_list:
            if u.user_id==user_id:
                user=u
                break
        for b in self.books_collection:
            if b.isbn==book_isbn:
                book=b
                break
        if user and book:
            user.borrow_book(book)
        else:
            print("User or Book not found")
    def perform_return(self,user_id=str,book_isbn=str):
        user=None
        book=None
        for u in self.users_list:
            if u.user_id==user_id:
                user=u
                break
        for b in self.books_collection:
            if b.isbn==book_isbn:
                book=b
                break
        if user and book:
            user.return_book(book)
        else:
            print("User or Book not found")
class Logger:
    @staticmethod
    def log_action(action=str):
        print(f"LOG: {action}")
    @staticmethod
    def log_error(error=str):
        print(f"ERROR: {error}")
