from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
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
    with sqlite3.connect("todo.db", timeout=10) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
    return render_template("index.html", tasks=tasks)

@app.route('/update_task')
def mark_as_done():
    return render_template('update.html')

@app.route("/summary")
def summary():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM tasks")
    total = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM tasks WHERE status='Done'")
    completed = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM tasks WHERE status='Pending'")
    pending = cur.fetchone()[0]

    conn.close()

    return render_template("summary.html", total=total, completed=completed, pending=pending)


# Add new task
@app.route("/tasks", methods=["POST"])
def add():
    task = request.form.get("task")
    status = request.form.get("status") or "Pending" 

    conn = sqlite3.connect("todo.db", timeout=10)  
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, status))
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/form")
def form():
    return render_template('form.html')

# Mark task as Done
@app.route("/update/<int:todo_id>")
def done(todo_id):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status='Done' WHERE id=?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect("/")

# Delete task
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
