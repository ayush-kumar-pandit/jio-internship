from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import time

def io_task(name,sec):
    print(f"{name} thread is starting for {sec} seconds")
    time.sleep(sec)
    return f" Thread {name} is Completed!!"

def cpu_task(name,sec):
    print(f"{name} process is starting for {sec} seconds")
    time.sleep(sec)
    return f" Process {name} is Completed!!"

if __name__ == "__main__":

    with ThreadPoolExecutor() as TPexecutor:
        results = TPexecutor.map(io_task,['A','B','C','D'],[1,3,2,4])
        for r in results:
            print(r)

    with ProcessPoolExecutor() as PPexecutor:
        results = PPexecutor.map(cpu_task,['P','Q','R','S'],[2,5,6,7])
        for r in results:
            print(r)
    
    