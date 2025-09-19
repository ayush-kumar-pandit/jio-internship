import csv

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
        
    def add_task(self,id,description):
        self.obj.append(task(id,description))


    def list_task(self):
        for row in self.obj:
            print(row)

    
    def save_to_csv(self):
        with open('To Do List.csv','a',newline = '')as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames = ['ID','Description','Status'])
            for row in self.obj:
                writer.writerow(row.dic)
        print('Data saved as CSV')

    
    def load_from_csv():
        pass
    



if __name__ == '__main__':
    TM = task_manager(1,'Install python 3.10+')

    TM.add_task(2,'Install Vs code')
    TM.add_task(3,'Setup GitHUb Account')

    TM.list_task()
    TM.save_to_csv()
        