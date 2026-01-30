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
# Note that we have named the file loaded as TASK_FILE variable for the function identification, and we have loaded the content 
# of the file if it exists, then we open and read it as a file from the os through this function.
# The tasks are stored in a dictionary with task IDs(task_id) as keys(tasks[int(task_id)]), and each task is represented as another dictionary containing the title and status.

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id},{task['title']},{task['status']}\n")
# Note that in this function, we are saving tasks that was created to receive the initial loaded contents of FILE_TASK variable to be formatted or manipulated.
# We open the file in write mode ('w') to iterate through the tasks dictionary, writing each task's ID, title, and status to the file in a comma-separated format.
# This ensures that the tasks dictionry has been copied into original file loaded and are persisted and can be reloaded later.

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
            # print(f"{task_id}\t{task['title']}\t{task['status']}")
            print(f"{task_id}\t{task.title}\t{task.status}")


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



# Main menu function to handle command line arguments using digits and interactive input
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
# Main menu function to handle command line arguments using string commands interactively
# def main():
#     tasks = load_tasks()
#     if len(sys.argv) < 2:
#         print("Usage: python commandline_taskmanager.py [add|display|complete|delete] [task_id]")
#         return

#     command = sys.argv[1]

#     if command == 'add':
#         add_task(tasks, title=None)
#     elif command == 'display':
#         display_tasks(tasks)
#     elif command == 'complete':
#         if len(sys.argv) < 3:
#             print("Please provide the task ID to mark as completed.")
#             return
#         task_id = int(sys.argv[2])
#         mark_task_completed(tasks, task_id)
#     elif command == 'delete':
#         if len(sys.argv) < 3:
#             print("Please provide the task ID to delete.")
#             return
#         task_id = int(sys.argv[2])
#         delete_task(tasks, task_id)
#     else:
#         print("Unknown command. Use add, display, complete, or delete.")

# if __name__ == "__main__":
#     main()



"""Additional Features to Implement:"""

# 1. Add deadlines or priorities to tasks.
# 2. Export tasks to different formats (e.g., CSV, JSON).
# 3. Support command-line arguments for quicker task management.
# 4. Implement search functionality to find tasks by keywords.


# Add deadlines or priorities to the task manager.
def add_deadlines(tasks, task_id, deadline):
    if task_id in tasks:
        tasks[task_id]['deadline'] = deadline
        print(f"Deadline '{deadline}' added to Task ID {task_id}.")
        save_tasks(tasks)
    else:
        print(f"Task ID {task_id} not found.")

def add_priorities(tasks, task_id, priority):
    if task_id in tasks:
        tasks[task_id]['priority'] = priority
        print(f"Priority '{priority}' added to Task ID {task_id}.")
        save_tasks(tasks)
    else:
        print(f"Task ID {task_id} not found.")

# Example usage of adding deadlines and priorities
# add_deadlines(tasks, 1, '2024-12-31')
# add_priorities(tasks, 1, 'High')        for task_id, task in tasks.items():
        #     print(f"{task_id}\t{task['title']}\t{task['status']}")        print("ID\tTitle\t\tStatus")
        # print("--\t-----\t\t------")            for task_id, task in tasks.items():
        #     print(f"{task_id}\t{task['title']}\t{task['status']}")            for task_id, task in tasks.items():



#Export tasks to different formats (e.g., CSV, JSON)
import json
import csv
def export_tasks_to_json(tasks, filename='tasks.json'):
    with open(filename, 'w') as json_file:
        json.dump(tasks, json_file)
    print(f"Tasks exported to {filename}")


def export_tasks_to_csv(tasks, filename='tasks.csv'):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Task ID', 'Title', 'Status'])
        for task_id, task in tasks.items():
            writer.writerow([task_id, task['title'], task['status']])



# Support command-line arguments for quicker task management.

def quick_command_line_interface():
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

# if __name__ == "__main__":
#     quick_command_line_interface()


# Implement search functionality to find tasks by keywords.
def search_tasks(tasks, keyword):
    found_tasks = {task_id: task for task_id, task in tasks.items() if keyword.lower() in task['title'].lower()}
    if found_tasks:
        print("Search Results:")
        for task_id, task in found_tasks.items():
            print(f"{task_id}\t{task['title']}\t{task['status']}")
    else:
        print("No tasks found with the given keyword.")
# Example usage of search functionality
# search_tasks(tasks, 'meeting')
