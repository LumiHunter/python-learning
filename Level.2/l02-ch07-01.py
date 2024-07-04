# AsyncIO: 비동기 I/O Coroutine 작업
# Generator: 반복적인 객체 Return 사용(yield)
# Non-blocking 비동기 처리

# Bloking I/O: 호출된 함수가 자신의 작업이 완료 될 때까지 제어권을 가지고 있음. 타 함수는 대기
# Non-blocking I/O: 호출된 함수(서브루틴)가 return(yield) 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속

# 스레드: 디버깅에 어려움, 자원 접근 시 경쟁상태, 데드락 문제.. -> 고려 후 코딩
# 코루틴: 하나의 루틴만 실행 -> 락 관리 필요X -> 제어권으로 실행 -> 사용함수가 비동기로 구현이 되어 있어야 하거나, 또는 직접 비동기로 구현해야 한다.

import asyncio
import timeit
from urllib.request import urlopen    # block 함수. 
from concurrent.futures import ThreadPoolExecutor
import threading

start = timeit.default_timer()

urls = ['http://daum.net', 'http://naver.com', 'https://tistory.com', 'https://wemakeprice.com']

async def fetch(url, executor):
    print('Thread Name: ', threading.current_thread(), 'Start', url)
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name: ', threading.current_thread(), 'Done', url)
    return res.read()[0:5]

async def main():
    # Non-block I/O: Thread Pool 생성
    executor = ThreadPoolExecutor(max_workers=10)
    # future 객체를 모아 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    result = await asyncio.gather(*futures)
    print()
    print('Result: ', result)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start

    print('Total Running Time: ', duration)