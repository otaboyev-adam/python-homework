import csv
import json
import math
import os
from datetime import datetime


# ---------------------------------------------------------------
# Small input helpers (used by Task 2 and Task 3)
# ---------------------------------------------------------------
def ask_text(prompt, allow_empty=False, no_commas=False):
    """Keep asking until the text is valid."""
    while True:
        value = input(prompt).strip()
        if value == "" and not allow_empty:
            print("This field can't be empty.")
        elif no_commas and "," in value:
            print("Please don't use commas.")
        else:
            return value


def ask_number(prompt):
    """Keep asking until the user types digits only."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print("Please enter a number (digits only).")


def ask_update(label, current, numeric=False, no_commas=False):
    """Ask for a new value. Pressing Enter keeps the current value."""
    while True:
        value = input(f"{label} ({current}), Enter to keep: ").strip()
        if value == "":
            return current
        if no_commas and "," in value:
            print("Please don't use commas.")
        elif numeric and not value.isdigit():
            print("Please enter a number (digits only).")
        else:
            return value


# ---------------------------------------------------------------
# Task 1: Generalized Vector Class
# ---------------------------------------------------------------
class Vector:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("A vector needs at least one component.")
        self.components = list(components)

    def __str__(self):
        # round(x, 3) keeps ints as ints (1 -> 1) and shortens floats
        values = ", ".join(str(round(c, 3)) for c in self.components)
        return f"Vector({values})"

    def check_same_dimension(self, other):
        if not isinstance(other, Vector):
            raise TypeError("This operation needs another Vector.")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of dimensions.")

    def __add__(self, other):
        self.check_same_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        self.check_same_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        # Vector * Vector -> dot product
        if isinstance(other, Vector):
            self.check_same_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        # Vector * number -> scalar multiplication
        if isinstance(other, (int, float)):
            return Vector(*[c * other for c in self.components])
        raise TypeError("Can only multiply a Vector by a Vector or a number.")

    def __rmul__(self, other):
        # number * Vector (e.g. 3 * v1)
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(c * c for c in self.components))

    def normalize(self):
        length = self.magnitude()
        if length == 0:
            raise ValueError("Cannot normalize the zero vector.")
        return Vector(*[c / length for c in self.components])


def task1():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print(v1)                 # Vector(1, 2, 3)
    print(v1 + v2)            # Vector(5, 7, 9)
    print(v2 - v1)            # Vector(3, 3, 3)
    print(v1 * v2)            # 32
    print(3 * v1)             # Vector(3, 6, 9)
    print(v1.magnitude())     # 3.7416573867739413
    print(v1.normalize())     # Vector(0.267, 0.535, 0.802)

    # Different dimensions -> error
    try:
        print(v1 + Vector(1, 2))
    except ValueError as error:
        print("Error:", error)


# ---------------------------------------------------------------
# Task 2: Employee Records Manager (OOP version)
# ---------------------------------------------------------------
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = int(salary)

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    @staticmethod
    def from_line(line):
        """Build an Employee from a line like: 1001, John Doe, Engineer, 75000"""
        parts = [p.strip() for p in line.split(",")]
        return Employee(*parts)  # wrong number of parts -> TypeError


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        try:
            open(self.filename, "a").close()  # create the file if missing
        except OSError as error:
            print("Could not create file:", error)

    # --- file handling ---
    def load_employees(self):
        employees = []
        try:
            with open(self.filename) as f:
                for line in f:
                    if line.strip():
                        try:
                            employees.append(Employee.from_line(line))
                        except (TypeError, ValueError):
                            print("Skipping bad line:", line.strip())
        except OSError as error:
            print("Could not read file:", error)
        return employees

    def save_employees(self, employees):
        try:
            with open(self.filename, "w") as f:
                for employee in employees:
                    f.write(str(employee) + "\n")
            return True
        except OSError as error:
            print("Could not save file:", error)
            return False

    def find_employee(self, employees, employee_id):
        for employee in employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    # --- menu operations ---
    def add_employee(self):
        employee_id = ask_number("Enter Employee ID: ")
        if self.find_employee(self.load_employees(), employee_id):
            print("Error: this Employee ID already exists.")
            return
        name = ask_text("Enter Name: ", no_commas=True)
        position = ask_text("Enter Position: ", no_commas=True)
        salary = ask_number("Enter Salary: ")

        employee = Employee(employee_id, name, position, salary)
        try:
            with open(self.filename, "a") as f:
                f.write(str(employee) + "\n")
            print("Employee added successfully!")
        except OSError as error:
            print("Could not save employee:", error)

    def view_all_employees(self):
        employees = self.load_employees()
        if not employees:
            print("No records found.")
            return

        sort_choice = input("Sort by: 1) none  2) name  3) salary: ").strip()
        if sort_choice == "2":
            employees.sort(key=lambda e: e.name.lower())
        elif sort_choice == "3":
            employees.sort(key=lambda e: e.salary)

        print("Employee Records:")
        for employee in employees:
            print(employee)

    def search_employee(self):
        employee_id = ask_number("Enter Employee ID to search: ")
        employee = self.find_employee(self.load_employees(), employee_id)
        if employee:
            print("Employee Found:")
            print(employee)
        else:
            print("Employee not found.")

    def update_employee(self):
        employees = self.load_employees()
        employee_id = ask_number("Enter Employee ID to update: ")
        employee = self.find_employee(employees, employee_id)
        if not employee:
            print("Employee not found.")
            return
        employee.name = ask_update("Name", employee.name, no_commas=True)
        employee.position = ask_update("Position", employee.position, no_commas=True)
        employee.salary = int(ask_update("Salary", employee.salary, numeric=True))
        if self.save_employees(employees):
            print("Employee updated successfully!")

    def delete_employee(self):
        employees = self.load_employees()
        employee_id = ask_number("Enter Employee ID to delete: ")
        employee = self.find_employee(employees, employee_id)
        if not employee:
            print("Employee not found.")
            return
        employees.remove(employee)
        if self.save_employees(employees):
            print("Employee deleted successfully!")

    def run(self):
        print("Welcome to the Employee Records Manager!")
        while True:
            print("\n1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")


def task2():
    EmployeeManager().run()


# ---------------------------------------------------------------
# Task 3: To-Do Application (CSV / JSON, easy to extend)
#
# Design (separation of concerns):
#   Task          -> only holds the data of one task
#   Storage       -> base class: "save(tasks)" and "load()"
#   CSVStorage / JSONStorage -> one class per file format
#   TodoManager   -> task logic (add, update, delete, filter), no printing
#   todo_menu()   -> the menu, the only part that talks to the user
#
# How to add a NEW format (e.g. XML) with minimal changes:
#   1. Write a new class (XMLStorage) that extends Storage and
#      implements save() and load().
#   2. Add ONE line to STORAGE_FORMATS:  "xml": XMLStorage
#   Nothing else changes: TodoManager and the menu only use the
#   save()/load() methods, and the format menu is built from the dict.
# ---------------------------------------------------------------
FIELDS = ["task_id", "title", "description", "due_date", "status"]
STATUSES = ["Pending", "In Progress", "Completed"]


class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date  # "" means no due date
        self.status = status

    def to_dict(self):
        return {field: getattr(self, field) for field in FIELDS}

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"],
                    data["due_date"], data["status"])

    def __str__(self):
        return (f"{self.task_id}, {self.title}, {self.description}, "
                f"{self.due_date or 'no due date'}, {self.status}")


# --- storage classes ---
class Storage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


class CSVStorage(Storage):
    def save(self, tasks):
        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, newline="") as f:
            return [Task.from_dict(row) for row in csv.DictReader(f)]


class JSONStorage(Storage):
    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=2)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename) as f:
            return [Task.from_dict(item) for item in json.load(f)]


# The ONLY place that lists the supported formats
STORAGE_FORMATS = {"csv": CSVStorage, "json": JSONStorage}


# --- task logic ---
class TodoManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = []
        self.load()  # load tasks on startup

    def save(self):
        try:
            self.storage.save(self.tasks)
            return True
        except OSError as error:
            print("Could not save tasks:", error)
            return False

    def load(self):
        try:
            self.tasks = self.storage.load()
            return True
        except (OSError, ValueError, KeyError) as error:
            print("Could not load tasks:", error)
            self.tasks = []
            return False

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def add_task(self, task):
        if self.find_task(task.task_id):
            return False  # ID already used
        self.tasks.append(task)
        return True

    def update_task(self, task_id, **changes):
        task = self.find_task(task_id)
        if not task:
            return False
        for field, value in changes.items():
            setattr(task, field, value)
        return True

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if not task:
            return False
        self.tasks.remove(task)
        return True

    def filter_by_status(self, status):
        return [task for task in self.tasks if task.status == status]


# --- user interface ---
def ask_due_date(prompt, current=""):
    """Optional date. Enter keeps/skips. Must look like YYYY-MM-DD."""
    while True:
        value = input(prompt).strip()
        if value == "":
            return current
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Please use the format YYYY-MM-DD.")


def ask_status(prompt, current=None):
    """Ask for a valid status (case-insensitive). Enter keeps the current one."""
    while True:
        value = input(prompt).strip().lower()
        if value == "" and current:
            return current
        for status in STATUSES:
            if value == status.lower():
                return status
        print("Status must be one of:", ", ".join(STATUSES))


def choose_storage():
    names = "/".join(STORAGE_FORMATS)  # built from the dict, so new formats appear automatically
    while True:
        fmt = input(f"Choose storage format ({names}): ").strip().lower()
        if fmt in STORAGE_FORMATS:
            return STORAGE_FORMATS[fmt](f"tasks.{fmt}")
        print("Unknown format, try again.")


def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("Tasks:")
    for task in tasks:
        print(task)


def todo_menu(manager):
    print("Welcome to the To-Do Application!")
    while True:
        print("\n1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            task_id = ask_text("Enter Task ID: ")
            title = ask_text("Enter Title: ")
            description = ask_text("Enter Description: ", allow_empty=True)
            due_date = ask_due_date("Enter Due Date (YYYY-MM-DD, Enter to skip): ")
            status = ask_status("Enter Status (Pending/In Progress/Completed): ")
            if manager.add_task(Task(task_id, title, description, due_date, status)):
                print("Task added successfully!")
            else:
                print("Error: this Task ID already exists.")

        elif choice == "2":
            print_tasks(manager.tasks)

        elif choice == "3":
            task_id = ask_text("Enter Task ID to update: ")
            task = manager.find_task(task_id)
            if not task:
                print("Task not found.")
            else:
                manager.update_task(
                    task_id,
                    title=ask_update("Title", task.title),
                    description=ask_update("Description", task.description),
                    due_date=ask_due_date(f"Due Date ({task.due_date or 'none'}), Enter to keep: ", task.due_date),
                    status=ask_status(f"Status ({task.status}), Enter to keep: ", task.status),
                )
                print("Task updated successfully!")

        elif choice == "4":
            task_id = ask_text("Enter Task ID to delete: ")
            if manager.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task not found.")

        elif choice == "5":
            status = ask_status("Enter status to filter by (Pending/In Progress/Completed): ")
            print_tasks(manager.filter_by_status(status))

        elif choice == "6":
            if manager.save():
                print("Tasks saved successfully!")

        elif choice == "7":
            if manager.load():
                print("Tasks loaded successfully!")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


def task3():
    storage = choose_storage()
    todo_menu(TodoManager(storage))


# ---------------------------------------------------------------
# Run the tasks
# ---------------------------------------------------------------
if __name__ == "__main__":
    while True:
        print("\n=== Lesson 7 Homework ===")
        print("1. Vector Class")
        print("2. Employee Records Manager (OOP)")
        print("3. To-Do Application")
        print("4. Quit")
        pick = input("Choose a task: ").strip()

        if pick == "1":
            task1()
        elif pick == "2":
            task2()
        elif pick == "3":
            task3()
        elif pick == "4":
            break
        else:
            print("Invalid choice.")
