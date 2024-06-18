# 시퀀스형에는 두 가지 종류가 있다.

# 컨테이너(Container): 서로 다른 자료형 -> 리스트, 튜플, collections.deque
# 플랫(Flat): 한 개의 자료형 -> 문자열(str), bytes, bytearray, array.array, memoryview

# 가변형(mutable): 리스트, bytearray, array.array, memoryview, collections.deque
# 불변형(immutable): 튜플, 문자열(str), bytes


# 지능형 리스트(Comprehending Lists)
chars = '+_)($##%(%*@)!)'
code_list1 = [ord(s) for s in chars]    # ord: 유니코드로 변경

# Comprehending Lists vs Map, Filter
code_list2 = [ord(s) for s in chars if ord(s) > 40]
code_list3 = list(filter(lambda x : x > 40, map(ord, chars)))

# Generator: 한 번에 한 개의 항목을 생성. 다음에 반환할 값만 가지고 있음. 메모리 유지X.(효율성 up)
import array
tuple_g = (ord(s) for s in chars)    # 리스트 컴프리헨션과 비슷하지만 소괄호 사용 혹은 소괄호 생략한 문장
array_g = array.array('I', (ord(s) for s in chars))    # integer를 의미하는 'I'와 generator를 인자로.
print(type(tuple_g))
print(next(tuple_g))
print(array_g)
print(type(array_g))
print(array_g.tolist())
print()

# ex_g = ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21))
# print(ex_g)
# for s in ex_g:
#     print(s)
# print()

# 리스트 생성 주의사항
marks1 = [['~'] * 5 for _ in range(3)]
print(marks1)    # 얕은 복사
marks2 = [['~'] * 5] * 3
print(marks2)    # 깊은 복사

print([id(i) for i in marks1])
print([id(i) for i in marks2])

# 수정 시 깊은 복사는 모두 영향을 받는다
marks1[0][2] = 'X'
marks2[0][2] = 'X'
print(marks1)
print(marks2)
print()

import copy
a = [1,2,3,[4,5,6]]
b = a    # identify
c = a.copy()    # 얕은 복사
d = copy.deepcopy(a)    # 깊은 복사
print(id(a), id(b), id(c), id(d))
print()
# 얕은 복사, 깊은 복사 모두 원본과 다른 id값을 가진다.

print([id(i) for i in a])
print([id(j) for j in c])
print([id(k) for k in d])   
print()
# 얕은 복사의 경우 모든 요소의 id가 원본과 같지만, 
# 깊은 복사는 요소 중 mutable 객체가 존재하면 id를 새롭게 할당한다.

a[0] = 0
print(b)
print(c) 
print(d)
print()
# a의 id가 1234, c의 id가 5678이면
# a[0]의 id와 c[0]의 id는 똑같이 abcd이다.
# 단, a[0]를 수정한다면 1234-abcd를 수정하는 것이므로 5678-abcd인 c[0]에는 영향이 없다!

a[3][0] = 0
print(b)
print(c)
print(d)
# a 내부의 mutable 객체인 a[3](리스트)의 id가 2468이면
# 얕은 복사의 결과물인 c 내부의 c[3]의 id도 2468로, '같은 주소값'을 바라보는 셈이 된다.
# 깊은 복사는 mutable 객체가 존재하면 id를 새롭게 할당하므로, d[3]의 id는 2468이 아니다.
# 즉, a[3]을 수정하면 c[3]도 함께 바뀌지만 d[3]에는 영향이 없다!