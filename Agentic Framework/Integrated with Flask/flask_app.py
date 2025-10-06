from flask import Flask,redirect,jsonify,request
import sqlite3
import psutil
import yaml
import time
from threading import Thread


app = Flask(__name__)
is_collecting = False
collector_thread = None

# Global flags

# Initialize DB
def init_db():
    conn = sqlite3.connect("sys_metrics.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpu FLOAT,
                    memory FLOAT,
                    disk FLOAT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    status TEXT
                )
                """)
    conn.commit()
    conn.close()

# Show current matrics on landing page
@app.route('/')
def index():
    return redirect('/metrics/data') 


# Select whether to start or stop collecting stats 
@app.route('/tasks/action', methods=['POST'])
def action():
    global is_collecting, collector_thread

    action = request.get_json('action')

    if action['action'] == 'start':
        if is_collecting:
            return jsonify({"message": "Already collecting"}), 200
        else:
            is_collecting = True
            collector_thread = Thread(target=background_collector, daemon=True)
            collector_thread.start()
            return jsonify({"message": "Started collecting system metrics"}), 200

    elif action['action'] == 'stop':
        if is_collecting:
            is_collecting = False
            return jsonify({"message": "Stopped collecting system metrics"}), 200
        else:
            return jsonify({"message": "Collection was not running"}), 200
        
    else:
        return jsonify({"message": "Something went wrong!!"}), 200



# Collects data in every 5 seconds
def background_collector():
    global is_collecting
    while is_collecting:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        try:
            with open('policy.yaml', 'r') as f:
                data = yaml.safe_load(f)
        except Exception as e:
            return jsonify({'error': f'Failed to load policy.yaml: {str(e)}'}), 500
        
        if (cpu < data['cpu']) and (mem < data['memory']) and (disk < data['disk']):
            status = 'healthy'
        else:
            status = 'breached'



        conn = sqlite3.connect('sys_metrics.db', timeout=10)
        cur = conn.cursor()
        cur.execute("INSERT INTO metrics (cpu, memory, disk, status) VALUES (?, ?, ?, ?)", (cpu, mem, disk, status))
        conn.commit()
        conn.close()

        time.sleep(5)



# Show live stats
@app.route('/metrics/data')
def live_stats():

    stat = {'cpu' : psutil.cpu_percent(),
            'memory' : psutil.virtual_memory().percent,
            'disk' : psutil.disk_usage('/').percent}
    return jsonify(stat)


# Show stats previously stored in database
@app.route('/metrics/dump')
def recent_stats():
    conn  = sqlite3.connect('sys_metrics.db', timeout = 10)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM metrics")
    rows = cur.fetchall()
    conn.close()
    
    stats = [dict(row) for row in rows]
    
    return jsonify(stats)

# Returns status whether resource usage is breached or not
@app.route('/health')
def status():
    try:
        with open('policy.yaml', 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return jsonify({'error': f'Failed to load policy.yaml: {str(e)}'}), 500

    conn = sqlite3.connect('sys_metrics.db', timeout=10)
    cur = conn.cursor()

    cur.execute("SELECT cpu, memory, disk FROM metrics ORDER BY rowid DESC LIMIT 1")
    row = cur.fetchone()
    conn.close()

    if row is None:
        return jsonify({'error': 'No metrics data found'}), 404

    cpu, mem, disk = row

    if (cpu < data['cpu']) and (mem < data['memory']) and (disk < data['disk']):
        return jsonify({'status': 'healthy'}), 200
    else:
        return jsonify({'status': 'breached'}), 500


if __name__ == '__main__':
    init_db()
    app.run(debug = True, threaded = True)