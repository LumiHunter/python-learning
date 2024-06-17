# 시퀀스형에는 두 가지 종류가 있다.

# 컨테이너(Container): 서로 다른 자료형 -> 리스트, 튜플, collections.deque
# 플랫(Flat): 한 개의 자료형 -> 문자열(str), bytes, bytearray, array.array, memoryview

# 가변형: 리스트, bytearray, array.array, memoryview, collections.deque
# 불변형: 튜플, 문자열(str), bytes


# 지능형 리스트(Comprehending Lists)
chars = '+_)($##%(%*@)!)'
code_list1 = [ord(s) for s in chars]    # ord: 유니코드로 변경

# Comprehending Lists + Map, Filter
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

ex_g = ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21))
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