import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks():
    tasks = load_tasks()
    print("\nTO-DO LIST:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✔ Task added.")

def delete_task():
    show_tasks()
    idx = int(input("Enter task number to delete: "))
    tasks = load_tasks()
    if 1 <= idx <= len(tasks):
        tasks.pop(idx-1)
        save_tasks(tasks)
        print("✔ Task deleted.")
    else:
        print("❌ Invalid task number.")

def menu():
    print("\n1) Show Tasks\n2) Add Task\n3) Delete Task\n4) Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice")
