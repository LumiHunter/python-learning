# AsyncIO: 비동기 I/O Coroutine 작업
# Generator: 반복적인 객체 Return 사용(yield)
# Non-blocking 비동기 처리

# Bloking I/O: 호출된 함수가 자신의 작업이 완료 될 때까지 제어권을 가지고 있음. 타 함수는 대기
# Non-blocking I/O: 호출된 함수(서브루틴)가 return(yield) 후 호출한 함수(메인 루틴)에 제어권 전달 -> 타 함수는 일 지속

# 스레드: 디버깅에 어려움, 자원 접근 시 경쟁상태, 데드락 문제.. -> 고려 후 코딩
# 코루틴: 하나의 루틴만 실행 -> 락 관리 필요X -> 제어권으로 실행 -> 사용함수가 비동기로 구현이 되어 있어야 하거나, 또는 직접 비동기로 구현해야 한다.

import asyncio
import timeit
from urllib.request import urlopen    # block I/O 함수. 
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트여야 편하다!
urls = ['http://daum.net', 'http://naver.com', 'http://tistory.com', 'http://wemakeprice.com']

async def fetch(url, executor):
    print('Thread Name: ', threading.current_thread(), 'Start', url)
    res = await loop.run_in_executor(executor, urlopen, url)
    soup = BeautifulSoup(res.read(), 'html.parser')
    # print(soup.prettify())    # 전체 페이지 소스 확인 
    result_data = soup.title
    print('Thread Name: ', threading.current_thread(), 'Done', url)
    return result_data

async def main():
    # Non-block I/O: Thread Pool 생성
    executor = ThreadPoolExecutor(max_workers=10)
    # future 객체를 모아 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]   # url 하나당 하나씩의 Thread
    result = await asyncio.gather(*futures)    # await -> yield인 셈!
    print()
    print('Result: ', result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()    # 루프 초기화
    loop.run_until_complete(main())    # 작업 완료까지 대기
    duration = timeit.default_timer() - start    # 수행 시간 계산
    print('Total Running Time: ', duration)