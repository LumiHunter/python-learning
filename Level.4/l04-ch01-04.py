"""
Section 1
Multithreading - Thread(2) - Daemon, Join
Keyword - DaemonThread, Join
"""
"""
DaemonThread(데몬 스레드)
    (1) 백그라운드에서 실행
    (2) 메인 스레드 종료 시, 즉시 종료됨 (일반 스레드는 메인 스레드 종료 시 함께 종료되는 것과 다름)
    (3) 주로 백그라운드 무한 대기 이벤트(while 문) 발생 실행하는 부분 담당 -> JVM(가비지 컬렉션), 자동저장 기능 등
"""
import logging
import threading
import time

# 스레드 실행 함수. 서브 스레드는 메인 스레드가 종료되어도 끝까지 실행됨.
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)
    
    for i in d:
        print(i)
        
    logging.info("Sub-Thread %s: finishing", name)

# 메인 영역
if __name__ == "__main__":
    # Logging format 설정. 멀티스레드는 디버깅이 어렵기 때문에 로그를 자주 남겨야 함.
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    # 함수 인자 확인
    # Daemon: Defalut는 False임.
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(10000)), daemon=True)
    
    logging.info("Main-Thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    y.start()
    
    # 데몬스레드 확인
    # print(x.isDaemon())
    
    # 데몬스레드인데 join을 사용할 경우, 반대로 메인스레드가 끝나도 끝까지 실행을 한 다음 종료됨 -> 권장되지 않음.
    # x.join()
    # y.join()
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread: all done")
    