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

# 파이썬 3.5 이상: def -> async, yield -> await (StopIteration 자동 처리)

# coroutine ex1
# def는 함수, 코루틴, 제네레이터를 모두 선언하는 예약어임!
def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine received: {}'.format(i))
    j = yield
    print('>>> coroutine received: {}'.format(j))
    
# 메인 루틴: 제네레이터 선언
cr1 = coroutine1()
print(cr1, type(cr1))    # 코루틴은? 제네레이터 타입이다!

# yield 지점까지 서브루틴 수행
next(cr1)

# send: yield에 값을 보냄
# next: yield에 None을 보냄(값을 보내지 않음)
try:
    cr1.send(100)
    next(cr1)
except StopIteration:
    print('StopIteration: There is no yield anymore.')
print()

# 잘못된 사용례
cr2 = coroutine1()
try:
    cr2.send(10)
    # yield에 멈춘 상태(GEN_SUSPENDED)에서 send를 보내야 함. 
    # 그러지 않으면(GEN_CREATED 상태) '값을 받을 곳이 없기 때문에' 에러 발생
except TypeError:
    print("Can't send non-value to a just-started generator.")
print()   

# coroutine ex2
# GEN_CREATED: 처음 대기 상태
# GEN_RUNNING: 실행 상태
# GEN_SUSPENDED: yield 대기 상태
# GEN_CLOSED: 실행 완료 상태

from inspect import getgeneratorstate

def coroutine2(x):
    print('>>> coroutine started: {}'.format(x))
    y = yield x
    print('>>> coroutine received: {}'.format(y))
    z = yield x + y
    print('>>> coroutine received: {}'.format(z))
    yield z
    
cr3 = coroutine2(10)
print(cr3)    # yield까지 실행되지 않았기 때문에, 아직 상태값이 없음.
print(getgeneratorstate(cr3))

print(next(cr3))    # next는 yield에 아무것도 보내지 않음
# y = yield x: "상태값(yield)은 x(10)" + "send를 통해 yield에 들어온 값은 y로 보낸다."
print(getgeneratorstate(cr3))

print(cr3.send(100))     # yield를 통해 y에 100을 보냄
# z = yield x + y: "상태값(yield)은 x + y(110)" + "send를 통해 yield에 들어온 값은 z로 보낸다."
print(getgeneratorstate(cr3))

print(cr3.send(200))    # yield를 통해 z에 200을 보냄
# yield z: "상태값(yield)은 z"
# 다음 yield가 없으므로, next 또는 send 실행 시 StopIteration 발생.
print(getgeneratorstate(cr3))
print()

# coroutine ex3
def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

t2 = generator1()
print(list(t2))
print()

def generator2():
    yield from 'AB'
    yield from range(1,4)

t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))