from library.exceptions import MemberLimitExceededException


class Member:
    MAX_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        if len(self.borrowed_books) >= Member.MAX_BOOKS:
            raise MemberLimitExceededException(self.name, Member.MAX_BOOKS)
        self.borrowed_books.append(book)

    def give_back(self, book):
        self.borrowed_books.remove(book)

    def __str__(self):
        titles = [book.title for book in self.borrowed_books]
        return f"{self.name} has: {titles}"
