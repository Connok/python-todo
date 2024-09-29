import tkinter as tk
from tkinter import simpledialog, messagebox
import json

def load_todos():
    try:
        with open('todos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open('todos.json', 'w') as f:
        json.dump(todos, f)

def add_todo():
    todo = simpledialog.askstring("Input", "Enter a new todo:")
    if todo:
        todos.append(todo)
        save_todos(todos)
        update_listbox()

def remove_todo():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        del todos[index]
        save_todos(todos)
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for todo in todos:
        listbox.insert(tk.END, todo)

# Create the main window
root = tk.Tk()
root.title("Desktop Todo App")

# Create and pack a listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Create and pack buttons
add_button = tk.Button(root, text="Add Todo", command=add_todo)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Todo", command=remove_todo)
remove_button.pack(pady=5)

# Load existing todos
todos = load_todos()
update_listbox()

# Start the GUI event loop
root.mainloop()