class Dog(object): # 'object' 상속
    # 클래스 변수: 클래스에서 직접 접근 가능, 공유
    species = 'firstdog'
    
    # __init__(): 클래스가 초기화될 때 반드시 한번 호출되는 함수
    # 인스턴스 변수: 객체마다 별도로 존재하고 해당 네임스페이스에 저장되는 변수
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 객체란: 소프트웨어로 구현할 대상. 클래스는 그 객체의 '틀'
    # 인스턴스란: 클래스를 가지고 만들어 낸 실체(객체)
    
print(Dog)

# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)
c = Dog('mikky', 2)

print(a == b, id(a), id(b))
print(a == c, id(a), id(c))    # 내용이 같아보여도 따로 초기화 된 다른 인스턴스임.

# 클래스 변수에 접근: 모든 인스턴스에서 다 같음
print(Dog.species)

# 네임스페이스: 객체가 저장된 공간 
# 인스턴스 변수는 인스턴스의 네임스페이스에 존재한다.
print(a.__dict__)
print(b.__dict__)

print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

print('-------------------------------------------------------------')

# 클래스에 __init__이 없다면 내부적으로 만들어진다.
# 단, 클래스가 초기화될 때 선언할 인스턴스 변수가 없으므로 만들지 않음.
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(f'{id(self)} has called')
        print('Func2 called')

f = SelfTest()
# print(dir(f))    # 인스턴스의 구성요소 들여다보기

try:
    f.func1()    # TypeError 발생
except Exception as e:
    print(e)    # func1은 self가 없는 '클래스 메소드'이므로 self를 받지 못함.
    
SelfTest.func1()    # 클래스로 직접 접근하여 호출해야 함.

print(id(f))    
f.func2()
SelfTest.func2(f)
# func2는 self를 받는 인스턴스 메소드임.
# func2는 selfTest를 인스턴스화 시킨 f를 받아야 한다.

print('----------------------------------------------')

class Warehause:
    stock_num = 0
    
    def __init__(self, name):
        self.name = name
        Warehause.stock_num += 1
        
    def __del__(self):    # 인스턴스가 소멸할 때(메모리에서 사라질 때 호출되는 함수)
        Warehause.stock_num -= 1
        
user1 = Warehause('Ryu')
user2 = Warehause('Cho')

print(Warehause.stock_num)

print(user1.name)
print(user2.name)

# 인스턴스는 클래스 변수를 공유받지만 네임스페이스를 호출할 때 클래스 변수가 표기되지는 않는다.
# 클래스 변수는 클래스의 네임스페이스에서 찾을 수 있다.
print(user1.__dict__)
print(user2.__dict__)
print(Warehause.__dict__)
print(user1.stock_num)

del user1
print(Warehause.__dict__)

print('-------------------------------------------------------------')

class Dog2:
    species = 'firstdog'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def bark(self, sound):
        return '{} says {}!'.format(self.name, sound)
    
j = Dog2('july', 4)
m = Dog2('merry', 5)

print(j.info())

print(j.bark('wal wal'))
print(m.bark('mung mung'))