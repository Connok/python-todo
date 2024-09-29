from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

def load_todos():
    if os.path.exists('todos.json'):
        with open('todos.json', 'r') as f:
            return json.load(f)
    else:
        return []
    
def save_todos(todos):
    with open('todos.json', 'w') as f:
        json.dump(todos, f)

@app.route('/')
def index():
    todos = load_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todos = load_todos()
    new_todo = request.form.get('todo')
    if new_todo:
        todos.append(new_todo)
        save_todos(todos)
    return redirect(url_for('index'))

@app.route('/remove/<int:index>')
def remove(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        del todos[index]
        save_todos(todos)
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)