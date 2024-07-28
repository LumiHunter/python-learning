'''
Python Variable Scope
Keywords: scope, glabal, nonlocal, locals, globals
'''
'''
전역변수는 주로 변하지 않는 고정 값에 사용함
지역변수 사용 이유: 지역변수는 함수 내의 로직 해결헤 국한, 소멸주기: 함수 실행 해제 시
전역변수를 지역 내에서 수정하는 것은 권장하지 않음!
'''

a = 10    # global variable

def foo():
    print(a)    # Read global variable
foo()

b = 20
def bar():
    b = 30    # local variable
    print(b)    # Read local variable
bar()

c = 40
def foobar():
    try:
        c = c + 10    # global 변수는 local scope에서 수정 불가.
    except UnboundLocalError:
        print("local variable 'c' referenced before assignment")
foobar()

d = 50
def barfoo():
    global d    # global 변수를 local scope에서 수정할 수 있으려면, global 키워드를 쓴다
    d = 60
    d += 100    # 그러나 전역변수는 '변하지 않는 변수'라는 전제가 있기 때문에, 권장되지는 않는다.
    print(d)

barfoo()

def outer():
    e = 70
    def inner():
        # UnboundLocall Error 상황: inner는 outer의 변수를 수정할 수 없음
        # e += 10
        nonlocal e    # inner의 변수를 받아 수정 가능할 수 있도록 하는 nonlocal 키워드
        e += 10
        print(e)
    return inner

in_test = outer()    # Closure
in_test()

def func(var):
    x = 10
    def printer():
        print('Printer Func Inner')
    print('Func Innter', locals())    # 해당 지역 scope에 있는 객체들을 모두 딕셔너리로 출력해줌
func('Hi')

print(globals())
for i in range(1,10):
    for j in range(1,10):
        globals()[f'mul_{i}_{j}'] = i*j
        
print(globals())
print(mul_2_2)    # globals() 딕셔너리에 직접 원소를 추가하는 방식으로도 전역변수를 생성할 수 있다.
