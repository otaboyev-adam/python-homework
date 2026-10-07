from library.book import Book
from library.member import Member
from library.exceptions import BookNotFoundException, BookAlreadyBorrowedException



class Library:
    def __init__(self):
        self.books = []
        self.members = []


    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

        print("Added book:", book)

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print("Added member:", name)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(title)

    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        raise ValueError(f"Member '{name}' does not exist.")

    def borrow_book(self, member_name, title):
        member = self.find_member(member_name)
        book = self.find_book(title)


        if book.is_borrowed:
            raise BookAlreadyBorrowedException(book.title)

        member.borrow(book)
        book.is_borrowed = True
        print(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member_name, title):
        member = self.find_member(member_name)
        book = self.find_book(title)

        if book not in member.borrowed_books:
            raise ValueError(f"{member.name} did not borrow '{book.title}'.")

        member.give_back(book)
        book.is_borrowed = False
        print(f"{member.name} returned '{book.title}'")

    def show_books(self):
        print("Books in the library:")
        for book in self.books:
            print(" -", book)
