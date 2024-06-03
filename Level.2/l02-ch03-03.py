# 파이썬의 핵심 -> 시퀀스, 반복, 함수, 클래스(Sequence, Iterator, Functions, Class)
# 스페셜 메소드(매직 메소드): 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드(Low level)
# 객체 -> 파이썬의 데이터를 추상화 -> 모든 객체는 id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt     # sqrt -> 루트
l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# Named Tuple
from collections import namedtuple
Point = namedtuple('Point', 'x y')    # Point 클래스
pt3 = Point(1.0, 5.0)    # Point 클래스의 인스턴스 생성
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)    # 인덱스로 접근할 때보다 clear!
print(l_leng2)

# Named Tuple 선언방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)    # rename default = False
# 키 x 중복 허용, 'class'라는 예약어를 키로 사용하는 경우이므로 본래는 오류가 생김!

print(Point1, Point2, Point3, Point4)

p1 = Point1(x = 10, y = 35)
p2 = Point2(20, 40)
p3 = Point3(45, y = 20)
p4 = Point4(10, 20, 30, 40)    # 중복된 x, 예약어 class는 난수 키로 할당됨 -> 난수 키가 필요할 때

temp_dict = {'x': 75, 'y': 55}
p5 = Point(**temp_dict)    # Dict Unpacking

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# Named Tuple Method
# _make(): 리스트로 새 객체 생성
temp = [12, 34]
p6  = Point1._make(temp)
print(p6)

# _fields: 필드 네임 확인
print(p1._fields, p4._fields)

# _asdict(): Orderd Dict 반환 -> Named Tuple을 Dictionary로 반환
print(p2._asdict())
print(p4._asdict())


# 사용 예시: 다량의 데이터 관리
Classes = namedtuple('Classes', 'rank, number')

students = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n) for n in range(1,21)]]    # List Comprehension
print(len(students))

for s in students:
    print(s)

# 헷갈림 주의
Cases = namedtuple('Classes', 'a b')    # 클래스 이름, 키 값들을 선언한 것이므로,
c = Cases(1,2)    # Cases라는 이름으로 인스턴스를 생성해도 해당 인스턴스는 Classes 클래스임!!
print(Cases)
print(type(c))