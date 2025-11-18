"""
Section 3
Concurrency, CPU Bound vs I/O bound - I/O bound(2) - threading vs asyncio vs multiprocessing
Keyword - I/O bound, requests, threading
"""
import aiohttp, time, asyncio

# ===== I/O bound asyncio 예제 =====
# threading보다 높은 복잡도 -> async, await, 비동기식으로 작동하는 패키지 필요.

async def request_site(session, url):
    print(session)
    print(session.headers)

    async with session.get(url) as response:
        print('Read Contents {0}, from {1}'.format(response.content_length, url))

async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        print(*tasks)
        print(tasks)
        await asyncio.gather(*tasks, return_exceptions=True)

def main():
    urls = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
        "http://realpython.com"
    ] * 5
    
    start_time = time.time()
    
    asyncio.run(request_all_sites(urls))
    
    duration = time.time() - start_time

    print()
    print(f'Download {len(urls)} sites in {duration} seconds')
    
if __name__ == "__main__":
    main()