import psutil
import yaml
import time
import csv



def display_usage(cpu_usage,mem_usage,disk_usage,bars = 50):
    cpu_percent = (cpu_usage / 100)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    disk_percent = (disk_usage / 100)
    disk_bar= '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))

    print(f"\rCPU usage : |{cpu_bar}| {cpu_usage:.2f}%  ", end = '')
    print(f"Memory usage : |{mem_bar}| {mem_usage:.2f}%  ", end = '')
    print(f"Disk usage : |{disk_bar}| {disk_usage:.2f}%  ", end = '\r')

    my_dict = {'CPU' : cpu_usage,
               'Memory' : mem_usage,
               'Disk' : disk_usage}


    with open('resource_usage.csv','a', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = ['CPU','Memory','Disk'])
        writer.writerow(my_dict)


    with open('policy.yaml','r') as f:
        data = yaml.safe_load(f)
    if (data['cpu'] < cpu_usage):
        print("\rCPU usage exceeded!!")
        exit()
    elif (data['mem'] < mem_usage):
        print("\rMemory usage exceeded!!")
    elif (data['disk'] < disk_usage):
        print("\Disk usage exceeded!!")
        exit()



while True:

    display_usage(psutil.cpu_percent(),psutil.virtual_memory().percent,psutil.disk_usage('C:/')[3],30)
    time.sleep(0.5)



