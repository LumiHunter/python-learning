# 파이썬의 핵심 -> 시퀀스, 반복, 함수, 클래스(Sequence, Iterator, Functions, Class)
# 스페셜 메소드(매직 메소드): 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드(Low level)

# 기본형: 자료형도 클래스다.
print(int)
print(float)

print(dir(int))    # 여기 나온 것들이 모두 매직 메소드!
print(dir(float))

n = 10
print(n + 100 == n.__add__(100))    # 단순 덧셈은 사실은 int 클래스에 구현된 __add__ 매직 메소드였다. 이용하기 쉽게 wrapping 된 것을 사용하는 것!
print(n.__doc__)
print(bool(n) == n.__bool__())
print(n * 100 == n.__mul__(100))

# 클래스 예제
class Fruit():
    # 파이썬 내부적으로 구현되어 있는 매직 메소드를 활용해 클래스를 만듦.
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __str__(self):
        return 'Fruit Class Info: {} , {}'.format(self._name, self._price)
    
    # 기존의 매직메서드 커스텀: 내 목적에 맞는 기능 효율적으로 개발 가능
    def __add__(self, x):
        print('20% discount')
        return self._price + x._price * 0.8
    
    def __sub__(self, x):
        return self._price - x._price
    
    def __le__(self, x):
        if self._price <= x._price:
            return True
        else:
            return False
        
    def __ge__(self, x):
        if self._price >= x._price:
            return True
        else:
            return False
    
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2)    # 앞에 호출된 인스턴스가 'self', 뒤가 'x'
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1)
print(s2)

# 일반적인 계산: 반복이 많고 복잡해짐!!!
# print(s1._price = s2._price)