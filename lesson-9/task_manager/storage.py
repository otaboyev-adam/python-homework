import json


def load_tasks(filename="tasks.json"):
    with open(filename) as file:
        return json.load(file)


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
