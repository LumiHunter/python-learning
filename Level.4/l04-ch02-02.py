"""
Section 2
Parallelism with Processing - Multiprocessing(1) - join, is_alive
Keyword - Multiprocessing, processing state
"""

from multiprocessing import Process
import time
import logging

def proc_func(name):
    print('Sub-Process {}: starting'.format(name))
    time.sleep(3)
    print('Sub-Process {}: finishing'.format(name))

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    p = Process(target=proc_func, args=('First',))

    logging.info('Main-Process: before creating Process')

    # 자식 프로세스 생성(메인 프로세스와 다름), 해당 프로세스에서 target 실행을 스케줄링: start()
    # 그러나, OS의 CPU 스케줄링은 '메인 프로세스' 우선!
    p.start()
    
    # 메인 프로세스를 재우면(blocked 상태, CPU 사용 X) 자식 프로세스가 먼저 실행될 수도 있음
    # 재우는 시간이 끝나면 바로 메인프로세스 runnable 상태로 복귀
    time.sleep(1)

    logging.info('Main-Processing: During Process')

    # 프로세스 강제 종료법: terminate(), 어떤 특정 조건(ex.시간 제한)을 두고 프로세스를 종료시킬 때 사용
    # logging.info('Main-Process: Terminated Process')
    # p.terminate()

    # 메인 프로세스를 block하여 자식 프로세스가 끝날 때까지 대기하도록 함 -> 자식 프로세스 결과를 정확히 받도록 보장하고, 언제 종료되었는지 제어하게 함: join()
    # 이제 OS는 자식 프로세스에게 CPU 시간을 할당
    logging.info('Main-Process: Joined Process')
    p.join()

    # 프로세스 상태 확인법: is_alive()
    print(f'Process p is alive: {p.is_alive()}')


if __name__ == "__main__":
    main()