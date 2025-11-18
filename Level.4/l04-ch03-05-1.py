"""
Section 3
Concurrency, CPU Bound vs I/O bound - I/O bound(1) - threading vs asyncio vs multiprocessing
Keyword - I/O bound, requests, threading
"""

import concurrent.futures
import threading
import requests, time

# ===== I/O bound threading 예제 ===== 
# 각 스레드에 생성되는 객체. 스레드는 메모리를 공유하지만 이건 예외! 독립적인 네임스페이스 영역을 사용함.
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def request_site(url):
    session = get_session()
    print(session)
    print(session.headers)
    
    with session.get(url) as response:
        print(f'Read Contents: {len(response.content)}, Status Code: {response.status_code} from {url}')

def request_all_sites(urls):
    # 멀티스레드 실행
    # 반드시 max_workers 개수 조절 후 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)

def main():
    urls = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
        "http://realpython.com"
    ] * 5
    
    start_time = time.time()
    
    request_all_sites(urls)
    
    duration = time.time() - start_time

    print()
    print(f'Download {len(urls)} sites in {duration} seconds')
    
if __name__ == "__main__":
    main()