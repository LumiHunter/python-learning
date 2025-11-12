"""
Section 1
Multithreading - Python GIL
Keyword - CPythin, 메모리 관리, GIL 사용 이유
"""
"""
GIL: Global Interpreter Lock
    (1) CPython -> Python(bytecode) 실행 시 여러 스레드 사용할 경우, 단일 스레드만이 Python object에 접근하게 제한하는 mutex
    (2) CPython의 메모리 관리가 취약하기 때문. 즉, 스레드를 안전하게 처리하기 위해
    (3) 단일 스레드로 충분히 빠름.
    (4) 멀티프로세스 사용 가능하므로 문제가 될 게 없음. (Numpy/Scipy 등 GIL 외부 영역에서 효율적인 코딩이 가능하게 만들어져 있음)
    (5) 병렬처리는 Multiprocessing, asyncio 사용 가능. 선택지 다양함.
    (6) 스레드 동시성 완벽처리를 위해 
"""