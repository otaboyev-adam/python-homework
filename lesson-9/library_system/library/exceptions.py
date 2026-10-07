
class BookNotFoundException(Exception):
    # Raised when a book is not in the library.


    def __init__(self, title):
        super().__init__(f"Book '{title}' was not found in the library.")


class BookAlreadyBorrowedException(Exception):
    # Raised when someone tries to borrow a book that is already taken.

    def __init__(self, title):
        super().__init__(f"Book '{title}' is already borrowed.")


class MemberLimitExceededException(Exception):
 # Raised when a member tries to borrow more books than allowed.

    def __init__(self, name, limit):
        
        super().__init__(f"{name} can't borrow more than {limit} books.")

