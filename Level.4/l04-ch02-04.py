"""
Section 2
Parallelism with Processing - Multiprocessing(3) - ProcessPoolExecutor
Keyword - ProcessPoolExecutor, as_completed, futures, timeout, dict
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

URLS = [
    'https://www.daum.net/',
    'https://www.cnn.com/',
    'https://www.naver.com/',
    'https://www.google.com/',
    'https://www.inflearn.com/'
]

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def main():
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드(예약. 실행이 아님)
        future_to_url = {executor.submit(load_url, url, 1): url for url in URLS}
        
        for future in as_completed(future_to_url):
            # Key 값이 Future 객체임
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' %(url, exc))
            else:
                print('%r page is %d bytes' %(url, len(data)))

if __name__ == "__main__":
    main()