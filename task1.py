import json
import os

class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title):
        self.tasks.append({"title": title, "done": False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        for i, t in enumerate(self.tasks, start=1):
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {status} {t['title']}")

    def update_task(self, idx, new_title):
        self.tasks[idx]["title"] = new_title
        self.save_tasks()

    def toggle_done(self, idx):
        self.tasks[idx]["done"] = not self.tasks[idx]["done"]
        self.save_tasks()

    def delete_task(self, idx):
        removed = self.tasks.pop(idx)
        self.save_tasks()
        return removed

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Mark task done/undone")
    print("5. Delete task")
    print("6. Exit")

def main():
    app = TodoApp()

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            if title:
                app.add_task(title)
                print("Task added!")
            else:
                print("Empty task not allowed.")

        elif choice == "2":
            app.view_tasks()

        elif choice == "3":
            app.view_tasks()
            if app.tasks:
                try:
                    idx = int(input("Task number to update: ")) - 1
                    if 0 <= idx < len(app.tasks):
                        new_title = input("New title: ").strip()
                        if new_title:
                            app.update_task(idx, new_title)
                            print("Task updated!")
                        else:
                            print("Empty title not allowed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid number.")

        elif choice == "4":
            app.view_tasks()
            if app.tasks:
                try:
                    idx = int(input("Task number to toggle done: ")) - 1
                    if 0 <= idx < len(app.tasks):
                        app.toggle_done(idx)
                        print("Task status changed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid number.")

        elif choice == "5":
            app.view_tasks()
            if app.tasks:
                try:
                    idx = int(input("Task number to delete: ")) - 1
                    if 0 <= idx < len(app.tasks):
                        removed = app.delete_task(idx)
                        print(f"Deleted: {removed['title']}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid number.")

        elif choice == "6":
            print("Bye! Your tasks are saved in tasks.json")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
