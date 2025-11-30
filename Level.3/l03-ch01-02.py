'''
Chapter 1
Python Advanced (1) - Python Variable Scope
Keyword - scope, global, nonlocal,locals, glabals
'''
'''
전역변수는 주로 변하지 않는 고정 값에 사용됨.
지역변수 사용 이유: 지역변수는 함수 내의 로직 해결에 국한, 소멸주기: 함수 실행 해제 시
전역변수가 지역 내에서 수정되는 것은 권장되지 않음
'''
# Ex1. 
a = 10  # Global variable

def foo():
    # Read global variable
    print('Ex1>', a)

foo()

# Ex2.
b = 20
def bar():
    b = 30  # local variable
    print('Ex2>', b)  
    # 파이썬은 로컬 스코프를 먼저 찾고 그 다음 전역스코프를 찾기 때문에, 30이 출력됨

bar()

# Ex3.
c = 40
def foobar():
    # c = c + 10
    # print('Ex3>', c)
    # UnboundLocalError: 로컬 스코프에서는 전역 변수를 수정할 수 없다. global 예약어 없이는.
    global c
    c = 60
    c += 100
    print('Ex3>', c)

foobar()
print('Ex4>', c)    # foobar()는 전역변수 c를 수정한 게 맞음.

# Ex4.
def outer():
    e = 70
    def inner():
        nonlocal e  # 지역변수 안에서 클로저 사용할 때 쓰는 예약어 nonlocal
        e +=10
        print('Ex5>', e)
    return inner

in_test = outer()  # Closure: 함수 inner가 반환됨
in_test()  # e = 80
in_test()  # e = 90. 변형된 값을 계속 '기억하고' 있기 위해 closure를 쓴다!

# Ex6.
def func(var):
    x = 10
    def printer():
        print('Ex6>', "Printer Func Inner")
    print("Func Inner", locals())  # 해당 지역 스코프에 어떤 객체가 있는지 dictionary로 보여줌

func('Hi')

# Ex7.
print('Ex7>', globals())
# test_variable = 100 이와 같이 변수를 선언하면
# 내부적으로 globals()['test_variable']=100 이런 방식으로,
# 변수를 하나 선언하면 locals(지역 스코프) 또는 globals(전역 스코프)에 key-value로 들어감

# Ex8. 지역 -> 전역 변수 생성
for i in range(1, 10):
    for k in range(1, 10):
        globals()['plus_{}_{}'.format(i, k)] = i + k

print(globals())
print(plus_5_5)  # 동적으로 변수 생성