# Task 1
# Name : Nidhi Gupta 
# Domain : Python

#A To-Do List application is a useful project that helps users manage and organize their tasks efficiently.
#This project aims to create a command-line or GUI-based application using Python, allowing 
#users to create, update, and track their to-do lists

import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.tasks = []

        # Frame for the listbox and scrollbar
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", width=15, command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", width=15, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", width=15, command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", width=15, command=root.quit)
        self.exit_button.pack(pady=5)

    def add_task(self):
        new_task = simpledialog.askstring("Input", "Enter a new task:")
        if new_task:
            self.tasks.append({"description": new_task, "completed": False})
            self.update_task_listbox()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = simpledialog.askstring("Input", "Enter the updated task:")
            if updated_task:
                self.tasks[selected_task_index[0]]['description'] = updated_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirm:
                self.tasks.pop(selected_task_index[0])
                self.update_task_listbox()
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]['completed'] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Mark as Completed", "Please select a task to mark as completed.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else "✗"
            self.task_listbox.insert(tk.END, f"{task['description']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
