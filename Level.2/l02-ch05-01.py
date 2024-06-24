# 일급 함수(일급 객체: First Class)
# 파이썬 함수의 특징 4가지
# 1. 런타임 초기화(실행 시점에 초기화)
# 2. 함수를 변수에 할당 가능
# 3. 함수를 다른 함수에 인수로 전달 가능
# 4. 함수를 결과로 반환 가능

def factorial(n):
    '''Factorical Function -> n : int'''
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))    # 함수만 가진 매직메소드
print(factorial.__name__)
print(factorial.__code__)
print()
# 즉, 함수는 객체다.

# 변수 할당
var_func = factorial
print(var_func(10))
print(list(map(var_func, range(1,11))))
print()

# 함수를 함수에 인수로 전달 및 함수로 결과 반환 -> Higher-order function
# map, filter: 인자를 하나씩 전달하므로, 인자를 하나만 받는 함수 필요
# reduce: 직전의 결과와 다음 인자를 하나씩 전달하므로, 인자를 두개 받는 함수 필요
print([var_func(i) for i in range(1,6) if i % 2])
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
# map에 var_func 함수를 인수로, filter에 lambda 함수를 인수로 전달

from functools import reduce
from operator import add
print(sum(range(1,11)))
print(reduce(add, range(1,11)))
# 익명함수 lambda는 가급적 주석을 달기를 권장됨.
# 일반함수 형태로 리팩토링하기를 권장함
print(reduce(lambda x, t: x + t, range(1,11)))
print()

# Callable: 호출 연산자 -> 메소드 형태로 호출 가능한지(~~() 형태로 부르기) 확인
print(callable(str), callable(A), callable(list), callable(var_func), callable(3.14))
print()

# inspect: 함수를 인자로 받는 함수들
from inspect import signature
sg = signature(var_func)
print(sg)
print(sg.parameters)
print()

# partial 사용법: 인수를 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial
print(mul(10, 10))
five = partial(mul, 5)
# mul의 인수 하나를 5로 고정함
# mul 함수를 함수의 인자로 전달했고,
# 그 결과로 함수가 반환되며, 
# 그것이 five라는 변수에 할당되었다.
print(five(10))
six = partial(five, 6)
print(six())    # five에 인자 6을 고정했으므로, 더는 줄 인자가 없이 그냥 호출!

print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))