'''
Keywords: lambda, map, filter, reduce
'''

'''
lambda 장점: 익명, 힙 영역 사용 즉시 소멸, pythonic, 파이썬 가비지 컬렉션
cf. 일반함수는 재사용성을 위해 메모리에 저장. 즉, 한번 쓰고 마는 것 -> lambda
시퀀스형 전처리에 Reduce, Map, filter 주로 사용
'''

digits1 = [x * 10 for x in range(1, 11)]
result = list(map(lambda i: i**2, digits1))
print(result)

# 이중함수 패턴
def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)
print(list(also_square(digits1)))

digits2 = list(range(1,11))
result = list(filter(lambda x: x % 2 == 0, digits2))
print(result)

def also_evens(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)
print(list(also_evens(digits2)))

from functools import reduce     # 내장함수가 아님!!
digits3 = list(range(1, 101))
result = reduce(lambda x, y: x+y, digits3)    # iterable을 순회하면서 func에서 지정해놓은 최종 누적 결과값을 내놓음(결과가 iterable 아님)
print(result)

def also_add(nums):
    def add_plus(x, y):
        return x + y
    return reduce(add_plus, nums)
print(also_add(digits3))