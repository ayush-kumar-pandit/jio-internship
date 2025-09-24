from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect("todos.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)
    conn.commit()
    conn.close()

# Show To-Do list
@app.route("/")
def index():
    conn = sqlite3.connect("todos.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos")
    todos = cur.fetchall()
    conn.close()
    return render_template("todo.html", todos=todos)

# Add new task
@app.route("/tasks", methods=["POST"])
def add():
    task = request.form.get("task")

    conn = sqlite3.connect("todos.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

    return redirect("/")

# Mark task as Done
@app.route("/done/<int:todo_id>")
def done(todo_id):
    conn = sqlite3.connect("todos.db")
    cur = conn.cursor()
    cur.execute("UPDATE todos SET status='Done' WHERE id=?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect("/")

# Delete task
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    conn = sqlite3.connect("todos.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id=?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
