# Simple To-Do List Check-In Application

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Completed Tasks")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks):
            status = "✅" if task['completed'] else "❌"
            print(f"{idx + 1}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter the task description: ")
    tasks.append({'title': title, 'completed': False})
    print("Task added successfully!")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_completed_tasks(tasks):
    tasks[:] = [task for task in tasks if not task['completed']]
    print("Completed tasks deleted.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
