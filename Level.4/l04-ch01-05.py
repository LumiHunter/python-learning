"""
Section 1
Multithreading - Thread(3) - ThreadPoolExecutor
Keyword - Many Threads, concurrent.futures, (xxx)PoolExecutor
"""
"""
그룹스레드
    (1) Python 3.2 이상 표준 라이브러리 사용
    (2) concurrent.futures
    (3) with 사용으로 스레드를 생성하거나 소멸하는 라이프사이클 관리 용이
    (4) 디버깅 어려움(단점)
    (5) 대기중인 작업 -> Queue(FIFO)에 담음 -> 완료 상태 조사 -> 결과 또는 예외 반환 -> 단일화(캡슐화)
"""
import logging
from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    logging.info('Sub-Thread %s: starting', name)
    time.sleep(2)
    result = 0
    for i in range(10001):
        result += i
    logging.info('Sub-Thread %s: finishing result: %d', name, result)
    
    return result
    
def main():
    # Logging format 설정. 멀티스레드는 디버깅이 어렵기 때문에 로그를 자주 남겨야 함.
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    logging.info("Main-Thread: befor creating and running thread")
    
    # 실행방법 1
    # excutor = ThreadPoolExecutor(max_workers=3)
    # task1 = excutor.submit(task, ('First', ))
    # task2 = excutor.submit(task, ('Second', ))
    
    # 결과 값이 있을 경우
    # print(task1.result())
    # print(task2.result())
    
    # max_workers : executor가 한번에 실행시키는 작업의 개수. 작업의 개수가 넘어가면 직접 설정이 유리
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = excutor.map(task, ['First', 'Second', 'Third', 'Fourth'])    # Fourth는 Third까지 묶음이 다 실행되고 나서 실행됨.
        print(list(tasks))

if __name__ == "__main__":
    main()