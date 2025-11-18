"""
Section 2
Parallelism with Processing - Process vs Thread, Parallelism
Keyword - Process, Thread, 병렬성
"""
"""
(1) Parallelism (병렬성)
    - 완전히 동일한 시점에 테스크를 실행
    - 다양한 파트로 나눠서 실행 (ex. 합을 나눠서 구하고 취합)
    - 멀티프로세싱에서 CPU가 1 Core인 경우는 만족하지 않음.
    - 딥러닝, 비트코인, 채굴 등.

(2) Process vs Thread
    - 독립된 메모리: 프로세스, 공유메모리: 스레드
    - 많은 메모리 필요: 프로세스, 적은 메모리: 스레드
    - 좀비(데드) 프로세서 생성 가능성 높음, 좀비(데드)스레드 생성 가능성은 높지 않음.
    - 오버해드 큼: 프로세스, 오버헤드 적음: 스레드
    - 생성과 소멸이 다소 느림: 프로세스, 생성과 소멸이 비교적 빠름: 스레드
    - 코드 작성이 쉬움/디버깅은 어려움: 프로세스, 코드 작성이 어려움/디버깅도 어려움: 스레드
"""
"""
동시성(Concurrency): 단일 CPU 코어에서. T1과 T2가 Context Switch를 통해 시간을 나누어 실행하는 것.
병렬성(Parallelism): 여러 CPU 코어에서 작업을 동시에 실행하는 것.

멀티스레드 프로세스에서 Code, Data, Heap은 공유되고 Stack만 따로
멀티프로세스에서는 모든 게 따로.
"""