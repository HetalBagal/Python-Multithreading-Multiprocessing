import multiprocessing
import time

lock = multiprocessing.Lock()

def square():
    for i in range(5):
        with lock:
            print(f"Square:{i*i}")
        time.sleep(2)


def cube():
    for i in range(5):
        with lock:
            print(f"Cube: {i*i*i}")
        time.sleep(2)


    
if __name__=="__main__" :
    ## Create the process
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    t=time.time()
    ##start the Process
    p1.start()
    p2.start()

    ## wait for the process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)







