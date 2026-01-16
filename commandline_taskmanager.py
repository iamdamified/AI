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

