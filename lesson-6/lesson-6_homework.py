import string
from collections import Counter


# ---------------------------------------------------------------
# Task 1: Zero Check Decorator
# ---------------------------------------------------------------
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper


@check
def div(a, b):
    return a / b


def task1():
    print(div(6, 2))   # 3.0
    print(div(6, 0))   # Denominator can't be zero


# ---------------------------------------------------------------
# Task 2: Employee Records Manager
# Record format: 1001, John Doe, Software Engineer, 75000
# ---------------------------------------------------------------
EMP_FILE = "employees.txt"


# --- input helpers (validation) ---
def ask_number(prompt):
    """Keep asking until the user types digits only."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print("Please enter a number (digits only).")


def ask_text(prompt):
    """Keep asking until the user types a non-empty text without commas."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("This field can't be empty.")
        elif "," in value:
            print("Please don't use commas.")
        else:
            return value


def ask_update(label, current, numeric=False):
    """Ask for a new value; pressing Enter keeps the current one."""
    while True:
        value = input(f"{label} ({current}), Enter to keep: ").strip()
        if value == "":
            return current
        if "," in value:
            print("Please don't use commas.")
        elif numeric and not value.isdigit():
            print("Please enter a number (digits only).")
        else:
            return value


# --- file helpers ---
def read_records():
    """Return all records as a list of lists: [id, name, position, salary]"""
    records = []
    try:
        with open(EMP_FILE) as f:
            for line in f:
                if line.strip():
                    records.append([p.strip() for p in line.split(",")])
    except FileNotFoundError:
        pass
    return records


def write_records(records):
    with open(EMP_FILE, "w") as f:
        for r in records:
            f.write(", ".join(r) + "\n")


def find_record(records, emp_id):
    """Return the record with this ID, or None."""
    for r in records:
        if r[0] == emp_id:
            return r
    return None


# --- menu options ---
def add_employee():
    emp_id = ask_number("Employee ID: ")
    if find_record(read_records(), emp_id):
        print("This ID already exists.")
        return
    name = ask_text("Name: ")
    position = ask_text("Position: ")
    salary = ask_number("Salary: ")
    with open(EMP_FILE, "a") as f:
        f.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee added.")


def view_employees():
    records = read_records()
    if not records:
        print("No records found.")
    for r in records:
        print(", ".join(r))


def search_employee():
    record = find_record(read_records(), ask_number("Enter Employee ID: "))
    if record:
        print(f"ID: {record[0]} | Name: {record[1]} | "
              f"Position: {record[2]} | Salary: {record[3]}")
    else:
        print("Employee not found.")


def update_employee():
    records = read_records()
    record = find_record(records, ask_number("Enter Employee ID to update: "))
    if not record:
        print("Employee not found.")
        return
    record[1] = ask_update("Name", record[1])
    record[2] = ask_update("Position", record[2])
    record[3] = ask_update("Salary", record[3], numeric=True)
    write_records(records)
    print("Employee updated.")


def delete_employee():
    records = read_records()
    record = find_record(records, ask_number("Enter Employee ID to delete: "))
    if not record:
        print("Employee not found.")
        return
    records.remove(record)
    write_records(records)
    print("Employee deleted.")


def task2():
    open(EMP_FILE, "a").close()  # create employees.txt if it doesn't exist
    while True:
        print("\n1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            break
        else:
            print("Invalid option, try again.")


# ---------------------------------------------------------------
# Task 3: Word Frequency Counter
# ---------------------------------------------------------------
def make_sample_file_if_missing(filename):
    try:
        open(filename).close()
    except FileNotFoundError:
        print(f"{filename} not found. Let's create it.")
        text = input("Type a paragraph: ")
        with open(filename, "w") as f:
            f.write(text)


def count_words(filename):
    """Read line by line (fine for large files). Return (total, Counter)."""
    counts = Counter()
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.lower().translate(str.maketrans("", "", string.punctuation))
            words = line.split()
            total += len(words)
            counts.update(words)
    return total, counts


def ask_top_n():
    """Bonus: user chooses how many top words to show (default 5)."""
    while True:
        value = input("How many top words to show? (Enter for 5): ").strip()
        if value == "":
            return 5
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a positive whole number.")


def show_results(total, top, n):
    print(f"Total words: {total}")
    print(f"Top {n} most common words:")
    for word, count in top:
        print(f"{word} - {count} {'time' if count == 1 else 'times'}")


def save_report(total, top, n, filename="word_count_report.txt"):
    with open(filename, "w") as f:
        f.write("Word Count Report\n")
        f.write(f"Total Words: {total}\n")
        f.write(f"Top {n} Words:\n")
        for word, count in top:
            f.write(f"{word} - {count}\n")
    print(f"Report saved to {filename}")


def task3():
    make_sample_file_if_missing("sample.txt")
    total, counts = count_words("sample.txt")
    n = ask_top_n()
    top = counts.most_common(n)
    show_results(total, top, n)
    save_report(total, top, n)