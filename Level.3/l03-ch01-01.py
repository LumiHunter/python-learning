'''
Chapter 1
Python Advanced (1) - Python Variable Scope
Keyword - scope, global, nonlocal,locals, glabals
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
    print("Func Inner", locals())

func('Hi')