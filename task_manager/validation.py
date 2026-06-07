from datetime import datetime

def validate_task_title(title):
    """
    Validates task title.
    Returns True if valid, False otherwise.
    """

    if len(title.strip()) == 0:
        print("Error: Title cannot be empty.")
        return False

    return True


def validate_task_description(description):
    """
    Validates task description.
    """

    if len(description.strip()) == 0:
        print("Error: Description cannot be empty.")
        return False

    return True


def validate_due_date(due_date):
    """
    Validates due date.
    """

    if len(due_date.strip()) == 0:
        print("Error: Due date cannot be empty.")
        return False

    return True