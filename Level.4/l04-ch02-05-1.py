"""
Section 2
Parallelism with Processing - Multiprocessing(4) - Sharing state
Keyword - memory sharing, array, value
"""

# 프로세스 메모리 공유 예제 (공유 X)

from multiprocessing import Process, current_process
import os

def generate_update_number(v: int):
    for _ in range(50):
        v += 1
    print(current_process().name, "data", v)
    
def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    print(f"Parent process ID: {parent_process_id}")

    # 프로세스 리스트
    processes = []
    
    # 프로세스 메모리 공유 변수
    share_value = 0
    
    for _ in range(1, 10):
        # 생성
        p = Process(target=generate_update_number, args=(share_value,))
        # 배열에 담기
        processes.append(p)
        # 실행
        p.start()
    
    for p in processes:
        p.join()
        
    # 최종 프로세스 부모 변수 확인 -> 변화 없다! 프로세스끼리는 원래 메모리 공유가 안되기 때문에 
    print('Final Data in parent process:', share_value)

if __name__ == "__main__":
    main()