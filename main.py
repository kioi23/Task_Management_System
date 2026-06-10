from task_manager.task_utils import (
    add_task,
    calculate_progress,
    mark_task_as_complete,
    tasks,
    view_pending_tasks,
)


def main():
    while True:
        print("\nTASK MANAGEMENT SYSTEM")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. View Pending Tasks")
        print("4. Track Progress")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date: ")

            add_task(tasks, title, description, due_date)

        elif choice == "2":
            title = input("Enter task title: ")
            mark_task_as_complete(tasks, title)

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            calculate_progress(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()