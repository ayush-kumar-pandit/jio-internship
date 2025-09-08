import tracemalloc

class My_Class:
    
    def __init__(self,name,size):
    
        self.data = [0] * size
        self.name = name
        print(f"{name} Created")
    


    
def test_mem_manage():
    
    tracemalloc.start()

    #take initial snapshot
    snap1 = tracemalloc.take_snapshot()

    obj1 = My_Class('Object 1',10000)

    #After creating an object
    snap2 = tracemalloc.take_snapshot()
    print("After creating object 1 :")
    for stat in snap2.compare_to(snap1,'lineno')[0:5]:
        print(stat)

    
    obj2 = My_Class('Object 2',20000)

    #After creating another object
    snap3 = tracemalloc.take_snapshot()
    print("After creating object 2 :")
    for stat in snap3.compare_to(snap1,'lineno')[0:5]:
        print(stat)

    
    # print(f"{obj1.name} deleted")
    del obj1

    #After deleting an object
    snap4 = tracemalloc.take_snapshot()
    print("After deleting object 1 :")
    for stat in snap4.compare_to(snap1,'lineno')[0:5]:
        print(stat)

    # print(f"{obj2.name} deleted")
    del obj2

    #After deleting an object
    snap5 = tracemalloc.take_snapshot()
    print("After deleting object 2 :")
    for stat in snap5.compare_to(snap1,'lineno')[0:5]:
        print(stat)

    current, peak = tracemalloc.get_traced_memory()
    print(f"\nCurrent memory usage: {current / 1024:.2f} KB")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")
    tracemalloc.stop()
    




if __name__ == "__main__":

    test_mem_manage()

    

    
