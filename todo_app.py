import json
import os

def save_todos(todos):
    with open('todos.json', 'w') as f:
        json.dump(todos, f)

def load_todos():
    if os.path.exists('todos.json'):
        with open('todos.json', 'r') as f:
            return json.load(f)
    else:
        return []

def remove_todo(todos, index):
    if 1 <= index <= len(todos):
        removed = todos.pop(index -1)
        print(f"Removed: {removed}")
    else:
        print("Invalid index")

def main(): 
    todos = load_todos() # Load todos at the start
    
    while True:
        command = input("Enter command (add/list/remove/quit): ").lower()
        
        if command == "quit":
            save_todos(todos) # Save todos before quiting
            break
        elif command == "add":
            task = input("Enter task: ")
            todos.append(task)
            print("Added:", task)
            save_todos(todos) # Save after adding
        elif command == "list":
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
        elif command == "remove":
            index = int(input("Enter index to remove: "))
            remove_todo(todos,index)
            save_todos(todos)
        else:
            print("Invalid command. Please try again")

if __name__ == "__main__":
    main()