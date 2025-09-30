from flask import Flask,redirect,jsonify
import sqlite3
import psutil
import yaml


app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect("sys_metrics.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            cpu FLOAT,
            memory FLOAT,
            disk FLOAT'
        )
    """)
    conn.commit()
    conn.close()

# Show current matrics on landing page
@app.route('/')
def index():
    return redirect('/metrics/data') 


# Select whether to start or stop collecting stats 
@app.route('/tasks/action', methods = ['POST'])
def action(act):
    while True:
        if act == 'Start':
            cpu_stat = psutil.cpu_percent()
            mem_stat = psutil.virtual_memory().percent
            disk_stat = psutil.disk_usage('/')

            conn = sqlite3.connect("sys_metrics.db", timeout = 10)  
            cur = conn.cursor()
            cur.execute("INSERT INTO metrics (cpu, memory, disk) VALUES (?, ?, ?)", (cpu_stat, mem_stat, disk_stat))
            conn.commit()
            conn.close()
        else:
            return redirect('/')



# Show live stats
@app.route('/metrics/data')
def live_stats():
    stat = {'cpu' : psutil.cpu_percent(),
            'memory' : psutil.virtual_memory().percent,
            'disk' : psutil.disk_usage('/')}
    return jsonify(stat)


# Show stats previously stored in database
@app.route('/metrics/dump')
def recent_stats():
    conn  = sqlite3.connect('sys_metrics.db', timeout = 10)
    cur = conn.cursor()

    cur.execute("SELECT * FROM metrics")
    stat = cur.fetchall()
    conn.close()

    return stat

# Returns status whether resource usage is breached or not
@app.route('/health')
def status():
    conn  = sqlite3.connect('sys_metrics.db', timeout = 10)
    cur = conn.cursor()

    cur.execute("SELECT cpu FROM metrics")
    cpu_usage = cur.fetchall()

    cur.execute("SELECT memory FROM metrics")
    mem_usage = cur.fetchall()
    
    cur.execute("SELECT disk FROM metrics")
    disk_usage = cur.fetchall()


    with open('policy.yaml','r') as f:
        data = yaml.safe_load(f)
    if (data['cpu'] > cpu_usage) and (data['mem'] > mem_usage) and (data['disk'] > disk_usage):
       return 200


if __name__ == '__main__':
    app.run(debug = True)