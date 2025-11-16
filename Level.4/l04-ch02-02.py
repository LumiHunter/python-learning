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

    p.start()

    logging.info('Main-Processing: During Process')

    # 프로세스 강제 종료법
    # logging.info('Main-Process: Terminated Process')
    # p.terminate()

    logging.info('Main-Process: Joined Process')
    p.join()

    print(f'Process p is alive: {p.is_alive()}')


if __name__ == "__main__":

    main()