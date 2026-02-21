## MultiThreading

import threading
import time

lock = threading.Lock()

def print_num():
    for i in range(5):
        with lock:
            print(f"Number:{i}")
        time.sleep(2)


def print_letter():
    for letter in 'abcde':
        with lock:
            print(f"Letter: {letter}")
        time.sleep(2)

## Create the thread
t1 =threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)

t=time.time()
##start the thread
t1.start()
t2.start()

## wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)
