"""
Section 1
Multithreading - Thread(4) - Lock, DeadLock
Keyword - Lock, DeadLock, Race Condition, Thread synchronizaion
"""

"""
(1) 세마포어(Semaphore): 공유 된 자원에 접근 시 지정된 개수의 프로세스/스레드만 접근 처리하도록 해 문제 발생 가능성을 막는 것 -> 경쟁상태 예방
    (하나 이상의 동기화 대상, 자원 소유 불가, 시스템 범위에 걸쳐 있음)
    
(2) 뮤텍스(mutex): 공유된 자원에 여러 스레드/프로세스가 접근하는 것을 막는 것 -> 경쟁상태 예방
    (하나의 동기화 대상, 자원 소유, 프로세스가 종료될 때 자동으로 clean up)

(3) Lock: 상호 배제를 위한 잠금 처리 -> 데이터 경쟁

(4) DeadLock: 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황 (교착 상태)

(5) Thread synchronization(스레드 동기화)

(6) 세마포어와 뮤텍스의 차이점은? 
    -> 세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용함
    -> 뮤텍스는 단일 스레드가 리소스 또는 중요 섹션을 소비하도록 허용
    -> 세마포어는 리소스에 대한 제한된 수의 동시 액세스를 허용
    -> 뮤텍스는 자원 소유권이 있어 획득한 스레드만 해제할 수 있지만, 세마포어는 자원 소유가 불가능하며 다른 스레드가 해제할 수 있음
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time

class FakeDataStore:
    pass

if __name__ == "__main__":
    # Logging Format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 클래스 인스턴스화
    store = FakeDataStore()
    
    logging.info("Testing update. Starting value is %d", store.value)
    
    # With Context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)
            
    logging.info("Testing update. Starting value is %d", store.value)