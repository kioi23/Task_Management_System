def validate_task_title(title):
    title = title.strip()
    return len(title) >= 3


def validate_task_description(description):
    description = description.strip()
    return len(description) >= 5


def validate_due_date(due_date):
    due_date = due_date.strip()
    return len(due_date) > 0