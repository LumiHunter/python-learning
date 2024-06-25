# 일급 함수(일급 객체: First Class)
# 데코레이터(Decorator)의 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크.... -> 공통 기능
# 3. 조합해서 사용 용이
# 단점: 가독성 감소(?), 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리함, 디버깅 불편

import time

def perf_clock(func):
    def perf_clocked(*args):
        st = time.perf_counter()    # 함수 시작 시간
        result = func(*args)    # 함수 실행
        et = time.perf_counter() - st    # 함수 종료 시간
        name = func.__name__    # 실행 함수명
        arg_str = ', '.join(repr(arg) for arg in args)    # 함수 매개변수 -> repr()는 str()와 유사하게 '문자열'을 출력한다.
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

# 데코레이터 미사용 - 함수를 직접 호출해야
def sleep_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)

none_deco1 = perf_clock(sleep_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func')
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_func')
none_deco2(100, 200, 300, 400)

# 데코레이터 사용 - 사용하고자 하는 함수에 @decorator만 붙이면 됨!
@perf_clock
def sleep_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

print('-' * 40, 'Called Decorator -> time_func')
sleep_func(1.5)
print('-' * 40, 'Called Decorator -> sum_func')
sum_func(100, 200, 300, 400)
