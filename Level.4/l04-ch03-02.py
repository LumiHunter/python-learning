"""
Section 3
Concurrency, CPU Bound vs I/O bound - Blocking vs Non Blocking IO (IO: 입출력!)
Keyword - Blocking IO, Non-Blocking IO, Sync, Async
"""

""" 
blocking IO vs Non-blocking IO

    blocking IO
    - 시스템 콜 요청 시 -> 커널이 IO 작업을 완료할 때까지 응답 대기
    - 제어권이 IO 작업에 있음 -> 커널이 소유 -> 응답(Response) 전까지 대기(Block) -> 다른 작업 수행 불가(대기)
    
    Non-blocking IO
    - 시스템 콜 요청 시 -> 커널 IO 작업 완료 여부 상관없이 즉시 응답
    - 제어권이 유저 프로세스에 있음 -> 다른 작업 수행 가능(지속)
    
    Async vs Sync
        - Async: IO 작업 완료 여부에 대한 알림이 커널(호출되는 함수) -> 유저프로세스(호출하는 함수) : 작업 다 되면 알아서 알려주기
        - Sync: IO 작업 완료 여부에 대한 알림이 유저프로세스(호출하는 함수) -> 커널(호출되는 함수) : 작업 다 됐는지 물어보기
"""