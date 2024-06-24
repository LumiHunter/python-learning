# 일급 함수(일급 객체: First Class)
# 파이썬의 변수 범위 'scope'

from typing import Any


b = 20    # global 변수
def func_v1(a):
    print(a)    # local 변수
    print(b)
func_v1(10)
print()

c = 30
def func_v2(a):
    print(a)    
    print(c)     # local 변수가 우선! global에 c가 있지만, 함수 안에 c가 있으므로 '선언 전에' c를 불러온 셈이 되어 error
    c = 40 
try:   
    func_v2(10)
except UnboundLocalError:
    print('"c" is a local variable in func_v2.')
print()

def func_v3(a):
    global c
    print(a)    
    print(c)
    c = 40    # global로 c를 받아왔으므로, 여기의 c는 global c와 같다. func_v3을 호출함으로써 c가 변한다!  
func_v3(10)
print(c)

# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 교착상태 문제를 처리하기 위해!
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 장점

a = 100
# 결과가 누적되지 않음
print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1,11)))

class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):    # 클래스를 함수처럼 '호출할 수 있음' -> Callable
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

averager_cls = Averager()    # _series 생성
print(dir(averager_cls))
print(averager_cls(10))    # averager_cls를 '호출'함으로써 __call__이 실행. _series에 값이 누적
print(averager_cls(30))    # 이전 실행의 결과를 '기억'함
print(averager_cls(50))
print(averager_cls(70))