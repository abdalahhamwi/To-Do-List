# to-do list
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                title, done = line.rstrip("\n").rsplit("|", 1)
                tasks.append({"title": title, "done": done == "1"})
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(f"{t['title']}|{'1' if t['done'] else '0'}\n")
    print("Tasks saved.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['title']}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added.")
    else:
        print("Empty title, not added.")

def mark_done(tasks):
    list_tasks(tasks)
    if not tasks: return
    try:
        idx = int(input("Task number to mark as done: "))
        tasks[idx - 1]["done"] = True
        print("Task marked as done.")
    except (ValueError, IndexError):
        print("Invalid number.")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks: return
    try:
        idx = int(input("Task number to delete: "))
        removed = tasks.pop(idx - 1)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid number.")

def menu():
    print("\n=== To‑Do List ===")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Mark Task as Done")
    print("4) Delete Task")
    print("5) Save Tasks")
    print("6) Load Tasks")
    print("0) Exit")

def main():
    tasks = load_tasks()
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
        elif choice == "6":
            tasks = load_tasks()
            print("Tasks loaded.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Unknown option.")

if __name__ == "__main__":
    main()
