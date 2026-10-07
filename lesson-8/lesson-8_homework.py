import math


# ---------------------------------------------------------------
# Task 1: Model a Farm
#
# Design:
#   Animal  (parent)  -> things ALL animals share: name, age, sound, food
#                        and behaviors: eat, sleep, make_sound
#   Cow, Chicken, Horse (children) -> inherit everything from Animal
#                        and add their own attribute + behavior
# ---------------------------------------------------------------
class Animal:
    def __init__(self, name, age, sound, food):
        self.name = name
        self.age = age
        self.sound = sound
        self.food = food

    def describe(self):
        kind = self.__class__.__name__  # "Cow", "Chicken", ...
        print(f"{self.name} is a {kind}, {self.age} years old.")

    def make_sound(self):
        print(f"{self.name} says: {self.sound}!")

    def eat(self):
        print(f"{self.name} is eating {self.food}.")

    def sleep(self):
        print(f"{self.name} is sleeping. Zzz...")


class Cow(Animal):
    def __init__(self, name, age, milk_per_day):
        super().__init__(name, age, "Moo", "grass")
        self.milk_per_day = milk_per_day  # liters

    def give_milk(self):
        print(f"{self.name} gives {self.milk_per_day} liters of milk per day.")


class Chicken(Animal):
    def __init__(self, name, age, eggs_per_week):
        super().__init__(name, age, "Cluck", "corn")
        self.eggs_per_week = eggs_per_week

    def lay_egg(self):
        print(f"{self.name} lays about {self.eggs_per_week} eggs per week.")


class Horse(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age, "Neigh", "hay")
        self.speed = speed  # km/h

    def gallop(self):
        print(f"{self.name} gallops at {self.speed} km/h!")


def task1():
    bessie = Cow("Bessie", 4, 20)
    clucky = Chicken("Clucky", 2, 5)
    thunder = Horse("Thunder", 6, 55)

    # The same methods work for every animal (inheritance)
    for animal in [bessie, clucky, thunder]:
        animal.describe()
        animal.make_sound()
        animal.eat()
        animal.sleep()
        print()

    # Behaviors that belong to one specific animal
    bessie.give_milk()
    clucky.lay_egg()
    thunder.gallop()


# ---------------------------------------------------------------
# Task 2: Bank Application
# accounts.txt format (one account per line): number,name,balance
# ---------------------------------------------------------------
class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return (f"Account Number: {self.account_number} | "
                f"Name: {self.name} | Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self, filename="accounts.txt"):
        self.filename = filename
        self.accounts = {}  # account_number -> Account
        self.load_from_file()  # load accounts when the program starts

    # --- file handling ---
    def save_to_file(self):
        try:
            with open(self.filename, "w") as f:
                for account in self.accounts.values():
                    f.write(f"{account.account_number},{account.name},{account.balance}\n")
        except OSError as error:
            print("Could not save accounts:", error)

    def load_from_file(self):
        try:
            with open(self.filename) as f:
                for line in f:
                    if line.strip():
                        try:
                            number, name, balance = line.strip().split(",")
                            self.accounts[int(number)] = Account(int(number), name, float(balance))
                        except ValueError:
                            print("Skipping bad line:", line.strip())
        except FileNotFoundError:
            pass  # first run, no file yet
        except OSError as error:
            print("Could not read accounts:", error)

    # --- helpers ---
    def check_amount(self, amount):
        if not math.isfinite(amount) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

    # --- bank operations (raise ValueError with a clear message on problems) ---
    def create_account(self, name, initial_deposit):
        if name == "" or "," in name:
            raise ValueError("Name can't be empty or contain commas.")
        if not math.isfinite(initial_deposit) or initial_deposit < 0:
            raise ValueError("Initial deposit can't be negative.")

        # unique number: one more than the biggest existing number
        account_number = max(self.accounts, default=1000) + 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        return account

    def view_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]

    def deposit(self, account_number, amount):
        account = self.view_account(account_number)
        self.check_amount(amount)
        account.balance += amount
        self.save_to_file()
        return account

    def withdraw(self, account_number, amount):
        account = self.view_account(account_number)
        self.check_amount(amount)
        if amount > account.balance:
            raise ValueError("Insufficient funds.")
        account.balance -= amount
        self.save_to_file()
        return account


# --- input helpers for the menu ---
def ask_int(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        raise ValueError("Please enter a whole number.")


def ask_float(prompt):
    try:
        return float(input(prompt).strip())
    except ValueError:
        raise ValueError("Please enter a valid number.")


def task2():
    bank = Bank()
    print("Welcome to the Bank Application!")
    while True:
        print("\n1. Create account")
        print("2. View account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter your name: ").strip()
                deposit = ask_float("Enter initial deposit: ")
                account = bank.create_account(name, deposit)
                print("Account created successfully!")
                print(account)
            elif choice == "2":
                number = ask_int("Enter account number: ")
                print(bank.view_account(number))
            elif choice == "3":
                number = ask_int("Enter account number: ")
                amount = ask_float("Enter deposit amount: ")
                account = bank.deposit(number, amount)
                print(f"Deposit successful! New balance: ${account.balance:.2f}")
            elif choice == "4":
                number = ask_int("Enter account number: ")
                amount = ask_float("Enter withdrawal amount: ")
                account = bank.withdraw(number, amount)
                print(f"Withdrawal successful! New balance: ${account.balance:.2f}")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        except ValueError as error:
            print("Error:", error)


# ---------------------------------------------------------------
# Run the tasks
# ---------------------------------------------------------------
if __name__ == "__main__":
    while True:
        print("\n=== Lesson 8 Homework ===")
        print("1. Model a Farm")
        print("2. Bank Application")
        print("3. Quit")
        pick = input("Choose a task: ").strip()

        if pick == "1":
            task1()
        elif pick == "2":
            task2()
        elif pick == "3":
            break
        else:
            print("Invalid choice.")