import csv
import logging
import pandas as pd


class Task:
    def __init__(self, id, description):
        self.dic = {
                    'ID': id,
                    'Description': description,
                    'Status': 'Pending'
                    }

    def __str__(self):
        return f"{self.dic['ID']},{self.dic['Description']},{self.dic['Status']}"


class TaskManager:
    def __init__(self, id, description):
        self.obj = [Task(id, description)]
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            filename='app.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='a'
        )

    def log(self, message):
        logging.info(message)

    def add_task(self, id, description):
        for row in self.obj:
            if row.dic['ID'] == id:
                print("Task already exists in List")
                return
        self.obj.append(Task(id, description))
        self.log(f"Task {id} added.")

    def update_status(self, id):
        for row in self.obj:
            if row.dic['ID'] == id:
                row.dic['Status'] = 'Completed'
                self.log(f"Task {id} marked as Completed.")
                return
        print("Task not found.")

    def list_tasks(self):
        for row in self.obj:
            print(row)

    def save_to_csv(self, filename='To Do List.csv'):
        data = [task.dic for task in self.obj]
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print('Data saved as CSV!!')
        self.log("Tasks saved to CSV.")

    def load_from_csv(self, filename='To Do List.csv'):
        try:
            df = pd.read_csv(filename)
            print(df.to_string(index=False))
        except FileNotFoundError:
            print("CSV file not found.")
            self.log("Attempted to load CSV but file not found.")

    def get_summary(self):
        data = [task.dic for task in self.obj]
        df = pd.DataFrame(data)
        print(f"Total number of tasks:{df['ID'].count()}")
        print(f"Total number of completed tasks:{df[df.Status == 'Completed'].count().Status}")
        print(f"Total number of pending tasks:{df[df.Status == 'Pending'].count().Status}")
        


if __name__ == '__main__':
    TM = TaskManager(1, 'Install python 3.10+')

    TM.add_task(2, 'Install Vs code')
    TM.add_task(3, 'Learn about Venv')
    TM.add_task(4, 'Setup Github account')
    TM.add_task(5, 'Master basic Git workflow')

    TM.list_tasks()

    TM.add_task(3, 'Learn about Venv')  
    TM.update_status(1)
    TM.update_status(2)
    TM.update_status(3)

    TM.save_to_csv()
    TM.load_from_csv()

    TM.get_summary()
