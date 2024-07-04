# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 
# -> '어디까지 했는지 마지막 시점을 기억하는 것': 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 
# -> '동시에 수행한 다음 수합하는 것' : 속도

# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> File, Network I/O 관련 작업 -> 동시성 활용 권장

# futures: 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선해서 나온 패키지
# concurrent.futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행 중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# GIL(Global Interface Lock): (Only Python) 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우
# -> 문제점을 방지하기 위해 GIL 실행, 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환) -> 싱글 스레드보다 오래 걸릴 수 있다!
# -> 멀티프로세싱을 사용하거나, CPython

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [100000, 1000000, 10000000, 1000000000]    
# 작업이 같은 시간이 걸린다는 보장, 다 성공한다는 보장이 없음!

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()
    # Futures
    futures_list = []

    # 결과 건수
    # ProcessPoolExcutor or ThreadPoolExecutor
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # 미래의 할일 반환
            future = excutor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()
        # wait 결과 출력
        # result = wait(futures_list, timeout=7)
        # # 성공
        # print('Completed Tasks: ' + str(result.done))
        # # 실패
        # print('Pending ones after waiting for 7 seconds:' + str(result.not_done))
        # print()
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):     # 먼저 끝나는 게 먼저 반환됨
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result: {}, Done : {}'.format(result,done))
            print('Future Cancelled: {}'.format(cancelled))
    # 종료 시간
    end_tm = time.time() - start_tm

    msg = '\n Time : {:.2f}s'
    print(msg.format(end_tm))

# 실행
if __name__ == '__main__':
    main()