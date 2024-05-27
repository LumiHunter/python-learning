"""
int: 정수
float: 실수
complex: 복소수
bool: 불린
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 딕셔너리
"""

# 숫자형 연산자
'''
+
-
*
/
//: 몫
%: 나머지
abs(x): 절대값
pow(x,y) = x ** y
'''

# 형 변환
a = 3.
b = 6
c = .7
d = 12.7

print(float(b))
print(int(c))    # float -> int: 소수점 절삭
print(int(True))    # True: 1, False: 0
print(float(False))
print(complex('3'))    # 문자형 -> 숫자형

print()

print(abs(-7))
x, y = divmod(100, 8)    # 몫, 나머지
print(x, y)
print(pow(5,3), 5**3)

print()
# 외부 모듈
import math
print(math.pi)
print(math.ceil(5.1))    # x 이상의 수 중에서 가장 작은 수 