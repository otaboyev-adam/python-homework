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
