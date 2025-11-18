"""
Section 3
Concurrency, CPU Bound vs I/O bound - I/O bound(1) - Synchronous
Keyword - I/O bound, requests
"""

import requests, time

def request_site(url, session):
    print(session)
    print(session.headers)
    
    with session.get(url) as response:
        print(f'[Read Contents: {len(response.content)}, Status Code: {response.status_code}] from {url}')

def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)

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