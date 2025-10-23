#Practice list, append , remove, while loop logic, input validation
# small cli-based interaction
# Demonstrates basic CRUD operations on a list

def display_tasks(tasks):
    if not tasks:
        print("\n No tasks available.\n")
        return
    print("\nYour TO-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ '{task}' added to your list.")
    else:
        print("⚠ Task cannot be empty.")

def remove_task(tasks):
    if not tasks:
        print("⚠ No tasks to remove.")
        return
    
    display_tasks(tasks)

    try: 
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑️ '{removed}' removed from your list.")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")
        
def main():
    tasks = []
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4)").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
