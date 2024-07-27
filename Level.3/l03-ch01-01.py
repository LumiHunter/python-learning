'''
Python Variable Scope
Keywords: scope, glabal, nonlocal, locals, globals
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