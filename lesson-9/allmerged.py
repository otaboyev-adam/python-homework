class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        if self.is_borrowed:
            status = "borrowed"
        else:
            status = "available"
        return f"{self.title} by {self.author} ({status})"















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























import csv


def read_grades(filename):
    students = []
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Grade"] = float(row["Grade"])
            students.append(row)
    return students


def calculate_averages(students):
    subjects = {}
    for student in students:
        subject = student["Subject"]
        if subject not in subjects:
            subjects[subject] = []
        subjects[subject].append(student["Grade"])

    averages = {}
    for subject, grades in subjects.items():
        average = round(sum(grades) / len(grades), 2)
        if average == int(average):
            average = int(average)
        averages[subject] = average
    return averages


def write_averages(averages, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, average in averages.items():
            writer.writerow([subject, average])



try:
    students = read_grades("grades.csv")
except FileNotFoundError:
    print("grades.csv was not found. Run the program from the student_grades folder.")
else:
    averages = calculate_averages(students)

    print("Average grades:")
    for subject, average in averages.items():
        print(f"{subject}: {average}")

    write_averages(averages, "average_grades.csv")
    print("Saved to average_grades.csv")







































import csv


def json_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])


















from storage import load_tasks, save_tasks
from stats import show_stats
from converter import json_to_csv


def show_tasks(tasks):
    print("ID | Task | Completed | Priority")
    for task in tasks:
        print(f"{task['id']} | {task['task']} | {task['completed']} | {task['priority']}")


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


try:
    tasks = load_tasks()
except FileNotFoundError:
    print("tasks.json was not found. Run the program from the task_manager folder.")
else:
    show_tasks(tasks)
    show_stats(tasks)

    answer = input("\nEnter a task ID to mark as completed (or press Enter to skip): ").strip()
    if answer != "":
        if answer.isdigit() and complete_task(tasks, int(answer)):
            save_tasks(tasks)
            print("Task updated and saved to tasks.json")
        else:
            print("No task with that ID.")

    json_to_csv(tasks)
    print("Tasks converted to tasks.csv")































def calculate_stats(tasks):
    total = len(tasks)

    completed = 0
    priority_sum = 0
    for task in tasks:
        if task["completed"]:
            completed += 1
        priority_sum += task["priority"]

    pending = total - completed

    if total > 0:
        average_priority = priority_sum / total
    else:
        average_priority = 0

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "average_priority": average_priority,
    }


def show_stats(tasks):
    stats = calculate_stats(tasks)
    print("\nTask statistics:")
    print("Total tasks:", stats["total"])
    print("Completed tasks:", stats["completed"])
    print("Pending tasks:", stats["pending"])
    print("Average priority:", round(stats["average_priority"], 2))



























import json


def load_tasks(filename="tasks.json"):
    with open(filename) as file:
        return json.load(file)


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
