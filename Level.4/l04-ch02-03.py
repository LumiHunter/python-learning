"""
Section 2
Parallelism with Processing - Multiprocessing(2) - Naming
Keyword - Naming, parallel processing
"""

from multiprocessing import Process, current_process
import os
import random
import time

def square(n):
    time.sleep(random.randint(1,3))
    process_id = os.getpid()
    process_name = current_process().name
    result = n*n
    print(f'Process ID: {process_id}, Process Name: {process_name}')
    print(f'Result of {n} square: {result}')

if __name__ == "__main__":
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    print(f'Parent process ID: {parent_process_id}')
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 생성 및 실행
    for i in range(1, 100):    # 여러개를 실행할 수록 코어 오버헤드가 올라감!
        t = Process(name=str(i), target=square, args=(i,))
        
        # 배열에 담기
        processes.append(t)
        # 실행
        t.start()
        
    for process in processes:
        process.join()
        
    # 종료
    print('Main-Processing Done!')