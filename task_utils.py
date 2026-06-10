from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

tasks = []


def add_task(tasks_list, title, description, due_date):
    if not validate_task_title(title):
        print("Invalid task title")
        return

    if not validate_task_description(description):
        print("Invalid task description")
        return

    if not validate_due_date(due_date):
        print("Invalid due date")
        return

    tasks_list.append(
        {
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date.strip(),
            "completed": False,
        }
    )
    print("Task added successfully")


def mark_task_as_complete(tasks_list, title):
    for task in tasks_list:
        if task["title"].lower() == title.strip().lower():
            task["completed"] = True
            print("Task marked as complete")
            return

    print("Task not found")


def view_pending_tasks(tasks_list):
    pending_tasks = [task for task in tasks_list if not task["completed"]]

    if len(pending_tasks) == 0:
        print("No pending tasks")
        return

    print("Pending Tasks:")
    for index, task in enumerate(pending_tasks, start=1):
        print(f"{index}. {task['title']} - {task['description']} (Due: {task['due_date']})")


def calculate_progress(tasks_list):
    if len(tasks_list) == 0:
        print("No tasks currently")
        return

    completed_tasks = 0
    for task in tasks_list:
        if task["completed"]:
            completed_tasks += 1

    total_tasks = len(tasks_list)
    progress = (completed_tasks / total_tasks) * 100
    print(f"Progress: {progress:.0f}% ({completed_tasks}/{total_tasks} completed)")


__all__ = [
    "add_task",
    "mark_task_as_complete",
    "view_pending_tasks",
    "calculate_progress",
    "tasks",
]