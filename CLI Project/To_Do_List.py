import csv

to_do_list = []
def add_task(task):
    my_dict = {'Task': task,'Status' : 'Pending'}
    to_do_list.append(my_dict)
    
def list_task():
    for item in to_do_list:
        print(item)

def mark_as_done(task):
    for item in to_do_list:
        if item['Task'] == task:
            item['Status'] = 'Completed'
    print('Updated!!')


def save_to_csv():
    with open('To Do List.csv',"w",newline = '') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = ['Task', 'Status'])
        for row in to_do_list:
            writer.writerow(row)
    print("Data stored as CSV file!!")

add_task('Install python 3.10+')
add_task('Install Vs Code')
add_task('Learn about venv')
add_task('Setup a Github account')
add_task('Master basic Git workflow')

list_task()

mark_as_done('Install python 3.10+')
mark_as_done('Install Vs Code')
list_task()
save_to_csv()
