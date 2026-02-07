import os

FILE_NAME = "tasks.txt"

def load_tasks():
    """خواندن کارها از فایل در ابتدای برنامه"""
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            # خواندن هر خط و حذف فاصله یا اینتر اضافی
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """ذخیره لیست کارها در فایل"""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n--- PERSISTENT TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = load_tasks()  # بارگذاری کارها در شروع برنامه
    
    while True:
        show_menu()
        choice = input("Choose (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("Your list is empty! 😊")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            save_tasks(tasks)  # ذخیره بعد از اضافه کردن
            print("Task saved! ✅")

        elif choice == '3':
            if not tasks:
                print("Nothing to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)  # ذخیره بعد از حذف کردن
                        print(f"Removed: {removed} 🗑️")
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Please enter a number.")

        elif choice == '4':
            print("Changes saved. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
