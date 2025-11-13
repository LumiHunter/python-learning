"""
Section 1
Multithreading - Thread(1) - Basic
Keyword - Threading basic
"""

import logging
import threading
import time

# 스레드 실행 함수. 서브 스레드는 메인 스레드가 종료되어도 끝까지 실행됨.
def thread_func(name):
    logging.info("Sub-Thread %s: starting", name)
    time.sleep(3)     # 시간이 소요되는 작업
    logging.info("Sub-Thread %s: finishing", name)

# 메인 영역
if __name__ == "__main__":
    # Logging format 설정. 멀티스레드는 디버깅이 어렵기 때문에 로그를 자주 남겨야 함.
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', ))
    
    logging.info("Main-Thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    
    # 메인 스레드가 서브 스레드가 끝날 때까지 기다리길 원할 경우
    x.join()
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread: all done")
    