import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        # Show a warning if the entry is empty
        messagebox.showwarning("Warning", "You must write something! ✍️")

# Function to delete the selected task
def delete_task():
    try:
        # Get the index of the selected item
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        # Show a warning if no task is selected
        messagebox.showwarning("Warning", "Please select a task to delete! 🗑️")

# Initialize the main window
root = tk.Tk()
root.title("Python To-Do List GUI 📝")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Header Label
label = tk.Label(root, text="What needs to be done?", font=("Arial", 14, "bold"), bg="#f0f0f0")
label.pack(pady=10)

# Entry field for new tasks
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)

# Add Button
add_button = tk.Button(root, text="Add Task ➕", command=add_task, bg="#4caf50", fg="white", font=("Arial", 10, "bold"))
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10, padx=20)

# Delete Button
delete_button = tk.Button(root, text="Delete Selected Task 🗑️", command=delete_task, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
delete_button.pack(pady=5)

# Start the application loop
if __name__ == "__main__":
    root.mainloop()
