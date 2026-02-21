### MultiProcess  with Process Pool Executor

from concurrent.futures import ProcessPoolExecutor
import time

def square(number):
    time.sleep(2)
    return f"Square : {number*number}"

numbers=[1,2,3,4,5,6]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3)as executor:
        results=executor.map(square,numbers)
    for result in results:
        print(result)

