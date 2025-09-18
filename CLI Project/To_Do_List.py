import csv

to_do_list = []
def add_task(task,id):
    my_dict = {'ID': id,'Task': task,'Status' : 'Pending'}
    to_do_list.append(my_dict)
    
def list_task():
    for item in to_do_list:
        print(item)

def mark_as_done(id):
    for item in to_do_list:
        if item['ID'] == id:
            item['Status'] = 'Completed'
    print('Updated!!')


def save_to_csv():
    with open('To Do List.csv',"w",newline = '') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = ['ID','Task', 'Status'])
        for row in to_do_list:
            writer.writerow(row)
    print("Data stored as CSV file!!")

add_task(task = 'Install python 3.10+',id = 1)
add_task(task = 'Install Vs Code',id = 2)
add_task(task = 'Learn about venv',id = 3)
add_task(task = 'Setup a Github account',id = 4)
add_task(task = 'Master basic Git workflow',id = 5)

list_task()

mark_as_done(1)
mark_as_done(2)
list_task()
save_to_csv()
