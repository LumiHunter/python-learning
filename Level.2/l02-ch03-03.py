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
Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)