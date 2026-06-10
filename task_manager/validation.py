def validate_task_title(title):
    title = title.strip()
    if len(title) == 0:
        raise ValueError("Task title cannot be empty.")

    if len(title) < 3:
        raise ValueError("Task title must be at least 3 characters long.")

    return True


def validate_task_description(description):
    description = description.strip()
    if len(description) == 0:
        raise ValueError("Task description cannot be empty.")

    if len(description) > 500:
        raise ValueError("Task description cannot exceed 500 characters.")

    return True


def validate_due_date(due_date):
    due_date = due_date.strip()
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty.")

    return True