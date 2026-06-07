from datetime import datetime
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):
    """
    Adds a task after validation.
    """

    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully")


def mark_task_as_complete(tasks, title):
    """
    Marks a task as complete.
    """

    for task in tasks:
        if task["title"].lower() == title.lower():

            task["completed"] = True

            print("Task marked as complete")
            return

    print("Task not found")


def view_pending_tasks(tasks):
    """
    Displays all incomplete tasks.
    """

    pending_found = False

    for task in tasks:

        if not task["completed"]:

            pending_found = True

            print("\nTitle:", task["title"])
            print("Description:", task["description"])
            print("Due Date:", task["due_date"])

    if not pending_found:
        print("No pending tasks")


def calculate_progress(tasks):
    """
    Calculates completion percentage.
    """

    if len(tasks) == 0:
        print("No tasks available")
        return

    completed_tasks = 0

    for task in tasks:

        if task["completed"]:
            completed_tasks += 1

    progress = (completed_tasks / len(tasks)) * 100

    print(f"Progress: {progress:.2f}%")