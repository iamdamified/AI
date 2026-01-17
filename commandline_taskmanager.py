# Command Line Task Manager
import sys
import os

# File to store tasks
TASK_FILE = 'tasks.txt'
# Load existing tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            for line in file:
                task_id, title, status = line.strip().split(',', 1)
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id},{task['title']},{task['status']}\n")


# Add a new task
def add_task(tasks, title):
    title = input("Enter task title: ").strip()
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "pending"}
    print(f"Task added with ID: {task_id}")
    save_tasks(tasks)


# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        # return
    else:
    # print("ID\tTitle\t\tStatus")
    # print("--\t-----\t\t------")
        for task_id, task in tasks.items():
            print(f"{task_id}\t{task['title']}\t{task['status']}")


# Mark a task as completed
def mark_task_completed(tasks, task_id):
    # task_id = int(input ("task ID to mark as completed: ")) do this if task_id not passed as argument
    if task_id in tasks:
        tasks[task_id]['status'] = 'completed'
        print(f"Task ID {task_id} marked as completed.")
        save_tasks(tasks)
    else:
        print(f"Task ID {task_id} not found.")


# Delete a task
def delete_task(tasks, task_id):
    # task_id = int(input("task ID to delete: ")) do this if task_id not passed as argument
    if task_id in tasks:
        del tasks[task_id]
        # tasks.pop(task_id, None)
        print(f"Task ID {task_id} deleted.")
        save_tasks(tasks)
    else:
        print(f"Task ID {task_id} not found.")



# Main menu function to handle command line arguments
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_task(tasks, title=None)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: ").strip())
            mark_task_completed(tasks, task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: ").strip())
            delete_task(tasks, task_id)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# or

def main():
    tasks = load_tasks()
    if len(sys.argv) < 2:
        print("Usage: python commandline_taskmanager.py [add|display|complete|delete] [task_id]")
        return

    command = sys.argv[1]

    if command == 'add':
        add_task(tasks, title=None)
    elif command == 'display':
        display_tasks(tasks)
    elif command == 'complete':
        if len(sys.argv) < 3:
            print("Please provide the task ID to mark as completed.")
            return
        task_id = int(sys.argv[2])
        mark_task_completed(tasks, task_id)
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Please provide the task ID to delete.")
            return
        task_id = int(sys.argv[2])
        delete_task(tasks, task_id)
    else:
        print("Unknown command. Use add, display, complete, or delete.")

if __name__ == "__main__":
    main()

