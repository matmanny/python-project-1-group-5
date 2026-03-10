tasks = []

while True:
    print("\nOptions: add | view | delete | complete | exit")
    choice = input("Enter your choice: ").lower()


    if choice == "add":
        task_input = input("Enter task with priority (example: Buy milk - high): ")
        parts = task_input.split("-")

        if len(parts) == 2:
            task_name = parts[0].strip()
            priority = parts[1].strip()
            tasks.append({"task": task_name, "priority": priority, "completed": False})
            print("Task added.")
        else:
            print("Invalid format. Use: Task - priority")

    
    elif choice == "view":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for i, t in enumerate(tasks, 1):
                status = "✓" if t["completed"] else "✗"
                print(f"{i}. {t['task']} | Priority: {t['priority']} | Completed: {status}")

   
    elif choice == "delete":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")

    
    elif choice == "complete":
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    
    elif choice == "exit":
        break

    else:
        print("Invalid option.")


completed = sum(1 for t in tasks if t["completed"])
pending = len(tasks) - completed

print("\n----- Summary -----")
print("Completed tasks:", completed)
print("Pending tasks:", pending)