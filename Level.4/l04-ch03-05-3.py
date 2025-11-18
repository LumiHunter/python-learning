"""
Section 3
Concurrency, CPU Bound vs I/O bound - I/O bound(2) - Asyncio basic
Keyword - asyncio
"""
""" 
동시 프로그래밍 패러다임 변화
싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 -> CPU 연산, DB 연동, API 호출 대기 시간 늘어남
파이썬 3.4 -> 비동기(asyncio) 표준라이브러리 등장
"""

import time
import asyncio

async def exe_calculate_async(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        await asyncio.sleep(1)
    print(f'{name} - {n} working done!')

async def process_async():
    start = time.time()
    # async def는 coroutine이지, task가 아니다.
    # asyncio.gather(python 3.11부터)는 coroutine을 자동으로 task로 변환해주고, 병렬로 실행할 수 있도록 해준다.
    # 모든 task가 끝날 때까지 기다리고, 각 coroutine의 return 값을 그대로 반환하므로, 전체 작업 병렬 실행에 최적화
    await asyncio.gather(
        exe_calculate_async('One', 3),
        exe_calculate_async('Two', 2),
        exe_calculate_async('Three', 1),
    )
    end = time.time()
    
    print(f'>>> total seconds: {end-start}')

def exe_calculate_sync(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        time.sleep(1)
    print(f'{name} - {n} working done!')

def process_sync():
    start = time.time()
    exe_calculate_sync('One', 3)
    exe_calculate_sync('Two', 2)
    exe_calculate_sync('Three', 1)
    end = time.time()
    
    print(f'>>> total seconds: {end-start}')

if __name__ == "__main__":
    # Sync 실행
    # process_sync()
    
    # Async 실행
    # Python 3.7 이상
    asyncio.run(process_async())
    # asyncio.get_event_loop().run_until_complete(process_async)