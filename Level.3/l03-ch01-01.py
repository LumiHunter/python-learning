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