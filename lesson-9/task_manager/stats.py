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
