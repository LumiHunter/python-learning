"""
Section 3
Concurrency, CPU Bound vs I/O bound - CPU bound(2) - Multiprocessing
Keyword - CPU Bound
"""

# CPU-bound Multiprocessing 예제

from multiprocessing import current_process, Array, Value, Manager, Process, freeze_support
import time, os

def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name

    print(f'Process ID: {process_id}, Process name: {process_name}')

    total_list.append(sum(i * i for i in range(number)))    # return 필요 없음. 

def main():
    numbers = [3_000_000 + x for x in range(30)]
    
    processes = []

    # 프로세스 공유 매니저
    manager = Manager()

    # 리스트 획득(프로세스 메모리 공유용)
    total_list = manager.list()

    start_time = time.time()
    
    for i in numbers:
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list, ))
        processes.append(t)
        t.start()
    
    for process in processes:
        process.join()

    print()
    print(f'Total list: {total_list}')
    print(f'Sum: {sum(total_list)}')

    duration = time.time() - start_time
    print()
    print(f'Duration: {duration} seconds')

if __name__ == "__main__":
    main()