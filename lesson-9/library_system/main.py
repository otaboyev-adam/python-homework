from library.library import Library
from library.exceptions import (
    BookNotFoundException,
    BookAlreadyBorrowedException,
    MemberLimitExceededException,
)


def borrow(lib, member_name, title):
    try:
        lib.borrow_book(member_name, title)
    except BookNotFoundException as e:
        print("Error:", e)
    except BookAlreadyBorrowedException as e:
        print("Error:", e)
    except MemberLimitExceededException as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)


def give_back(lib, member_name, title):
    try:
        lib.return_book(member_name, title)
    except BookNotFoundException as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)


lib = Library()

print("--- Adding books and members ---")
lib.add_book("Python Basics", "John Smith")
lib.add_book("Learn OOP", "Anna Brown")
lib.add_book("Data Structures", "Mike Lee")
lib.add_book("Web Development", "Sara Kim")
lib.add_book("Algorithms", "Tom Green")
lib.add_member("Ali")
lib.add_member("Vali")

print("\n--- Borrowing books ---")
borrow(lib, "Ali", "Python Basics")
borrow(lib, "Ali", "Learn OOP")
borrow(lib, "Ali", "Data Structures")

print("\n--- Breaking the rules ---")
borrow(lib, "Ali", "Web Development")     
borrow(lib, "Vali", "Python Basics")      
borrow(lib, "Vali", "Harry Potter")   
borrow(lib, "Hasan", "Algorithms")       
give_back(lib, "Vali", "Learn OOP")  

print("\n--- Returning books ---")
give_back(lib, "Ali", "Python Basics")
borrow(lib, "Vali", "Python Basics")  

print()
lib.show_books()
