import csv
import logging


class task:
    def __init__(self,id,description):
        self.dic = {'ID' : id,
                    'Description' : description,
                    'Status' : 'Pending'}
    
    def __str__(self):
        return f"{self.dic['ID']},{self.dic['Description']},{self.dic['Status']}"

class task_manager():
    
    def __init__(self,id,description):
        self.obj = [task(id,description)]
        


    def log(task_manager):
    
        logging.basicConfig(filename = 'app.log',
                            level = logging.INFO,
                            format = '%(asctime)s - %(levelname)s - %(message)s',
                            filemode = 'a')
        logging.info('Item added to list!!')
        for row in task_manager.obj:

            if type(row.dic['ID']) != int or type(row.dic['Description']) != str or type(row.dic['Status']) != str:
                logging.warning('Invalid input!!')


    def add_task(self,id,description):

        for row in self.obj:
            if row.dic['ID'] == id:
                print("Task already exists in List")
                return
        self.obj.append(task(id,description))
        

    def update_status(self,id):
        for row in self.obj:
            if row.dic['ID'] == id:
                row.dic['Status'] = 'Completed'

    def list_task(self):
        for row in self.obj:
            print(row)

    
    def save_to_csv(self):
        with open('To Do List.csv','a',newline = '')as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames = ['ID','Description','Status'])
            for row in self.obj:
                writer.writerow(row.dic)
        print('Data saved as CSV!!')

    
    def load_from_csv(self):
        print('Data retrieved from CSV!!')
        with open('To Do List.csv',newline = '')as csv_file:
            reader = csv.DictReader(csv_file,fieldnames = ['ID','Description','Status'])
            for row in reader:
                print(row['ID'],row['Description'],row['Status'])
    



if __name__ == '__main__':
    TM = task_manager(1,'Install python 3.10+')

    TM.add_task(2,'Install Vs code')
    TM.add_task(3,'Learn about Venv')
    TM.add_task(4,'Setup Github account')
    TM.add_task(5,'Master basic Git workflow')


    TM.list_task()

    TM.add_task(3,'Learn about Venv')
    TM.update_status(1)
    TM.update_status(2)
    TM.update_status(3)
    TM.save_to_csv()
    TM.load_from_csv()
    
    TM.log()
   

        