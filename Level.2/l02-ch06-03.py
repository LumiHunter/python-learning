# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 
# -> '어디까지 했는지 마지막 시점을 기억하는 것': 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 
# -> '동시에 수행한 다음 수합하는 것' : 속도

# 코루틴(Coroutine): 단일 스레드, 스택을 기반으로 동작하는 비동기 작업 
# -> 단일 스레드에서 여러 작업이 순차적으로 상호작용하면서 수행되는 패턴
# yield: 메인루틴 <-> 서브루틴 데이터 교환
# 코루틴 제어: 상태 저장, 양방향 전송

# 서브루틴: 메인루틴에서 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴: 루틴 실행 중 중지 -> 동시성 프로그래밍 -> 쓰레드에 비해 오버헤드 감소
# 쓰레드: 싱글스레드 -> 멀티스레드 -> 공유되는 자원으로 인해 교착상태 발생 가능성
# -> 멀티스레딩 시 컨텍스트 스위칭 비용이 발생해 자원 소비 가능성 증가

# coroutine ex1
# def는 함수, 코루틴, 제네레이터를 모두 선언하는 예약어임!
def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine received: {}'.format(i))
    
# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()
print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
next(cr1)

# yield에 100을 보냄(기본 값(next 사용 시)은 None)
#cr1.send(100)

# 잘못된 사용례
cr2 = coroutine1()
try:
    cr2.send(10)
    # yield에 멈춘 상태에서 send를 보내야 함. 
    # 그러지 않으면 '값을 받을 곳이 없기 때문에' 에러 발생
except TypeError:
    print("Can't send non-value to a just-started generator.")