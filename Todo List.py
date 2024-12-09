class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"description": task, "completed": False})
        print(f"Task added: {task}")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks in the list.")
            return

        for index, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['description']}")

    def complete_task(self, task_index):
        """Mark a task as completed."""
        try:
            index = task_index - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]["completed"] = True
                print(f"Task '{self.tasks[index]['description']}' marked as completed.")
            else:
                print("Invalid task number.")
        except IndexError:
            print("Invalid task number.")

    def remove_task(self, task_index):
        """Remove a task from the list."""
        try:
            index = task_index - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                print(f"Task '{removed_task['description']}' removed.")
            else:
                print("Invalid task number.")
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_num = int(input("Enter the task number to complete: "))
            todo_list.complete_task(task_num)
        elif choice == '4':
            todo_list.view_tasks()
            task_num = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_num)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()