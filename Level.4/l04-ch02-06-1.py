"""
Section 2
Parallelism with Processing - Multiprocessing(4) - Queue, Pipe
Keyword - Queue, Pipe, Commuications between processes
"""

# 프로세스 통신 구현: Queue

from multiprocessing import Process, Queue, current_process
import time, os

# 실행함수
def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name
    
    sub_total = 0
    for _ in range(baseNum):
        sub_total += 1
        
    # Produce
    q.put(sub_total)
    
    print(f'Process ID: {process_id}, Process name: {process_name}, ID: {id}')
    print(f'Result: {sub_total}')

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    print(f"Parent process ID: {parent_process_id}")
    
    # 프로세스 리스트
    processes = []
    
    # 시작 시간
    start_time = time.time()
    
    # Queue 선언
    q = Queue()
    
    for i in range(5):
        t = Process(name=str(i), target=worker, args=(i, 100000000, q))
        processes.append(t)
        t.start()
        
    for process in processes:
        process.join()
        
    # 순수 계산 시간
    print("--- %s seconds " %(time.time()-start_time))
    
    # 종료 플래그
    q.put('exit')
    
    total = 0
    
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp
            
    print()
    print('Main-Processing Total Count = {}'.format(total))
    print('Main-Processing is done!')
       
if __name__ == "__main__":
    main()