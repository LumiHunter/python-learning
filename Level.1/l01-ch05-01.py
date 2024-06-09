# def function_name(parameter):
#   code

def first_func(w):
    print("Hello,", w)
word = 'Good boy'
first_func(word)
print(type(first_func))
first_func    # function class 객체이므로 개행(괄호 여닫기)하지 않으면 아무 일도 일어나지 않음

def return_func(w1):
    return "Hello, " + str(w1)
x = return_func('Good girl')
print(x)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)

def func_mul2(x):    # 튜플형 반환 (리스트, 집합, 딕셔너리도 됨)
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

a, b, c = func_mul2(10)
q = func_mul2(10)

def args_func(*args):    # 언패킹-튜플 형태가 넘어올 때 많이 사용됨. 가변인자-몇개든 상관없음.
    for i, v in enumerate(args):
        print('Result: {}'.format(i), v)
    print('-----')
args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

def kwargs_func(**kwargs):    # 딕셔너리 언패킹
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('-----')
kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')    # {} 필요없음.

def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)
# 인자를 알아서 튜플/딕셔너리로 묶어줌!
print()

def nested_func(num):    # 중첩함수: 함수 안에서 함수 정의
    def func_in_func(num):    # func_in_func는 따로 호출 불가능
        print(num)
    print('In func')
    func_in_func(num+100)

nested_func(100)
print()

# 람다-'이름없는 함수': 메모리 절약, 가독성 향상, 코드 간결
# 일반 함수는 객체를 생성하므로 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 단, 남발 시 가독성 오히려 감소

lambda_to_variable = lambda x,y: x*y

def func_final(x,y,func):
    print(x * y * func(100,100))
func_final(10,20,lambda x, y: x + y)
func_final(10, 20, lambda_to_variable)