# 일급 함수(일급 객체: First Class)
# 클로저: 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장(스냅샷) -> 후에 접근(엑세스) 가능

# Closure 사용 패턴
def closure_ex1():
    # Free variable(클로저 영역) -> 사용하려고 하는 함수 바깥에 선언된 변수
    series = []
    def averager(v):
        series.append(v)
        print('inner >> {}/{}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()
print(avg_closure1(10))
print(avg_closure1(20))

avg_closure2 = closure_ex1()
print(avg_closure2(30))
print(avg_closure2(40))
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)
print()

# 잘못된 클로저 사용
def closure_ex3():
    cnt = 0
    total = 0
    def averager(v):
        # averager 함수 안부터 먼저 본다! 05-02의 func_v2와 같이, 
        # 이것은 averager의 local 변수가 아닌 cnt와 total을 '선언 전에' 불러온 셈이 된다!
        cnt += 1    
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
try:
    print(avg_closure3(10))
except UnboundLocalError:
    print('"cnt" and "total" are called before declaration.')
print()

def closure_ex4():
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total    # cnt와 total이 averager 함수의 local variable이 아닌 free variable이 됨
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure4 = closure_ex4()
print(avg_closure4(10))
print(avg_closure4(30))