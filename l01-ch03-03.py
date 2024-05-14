# 리스트 자료형 -> 순서O 중복O 수정O 삭제O

a = []
b = list()
c = [70, 75, 80, 85]
d = [100, 100.1, 'Ace', 'Base', 'Captine']
e = [100, 100.1, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

print(c + d)
print(c * 3)
print('Test' + str(c[0]))    # 문자 + 숫자 -> 연산 불가(str이 시퀀스 형이기 때문에, +는 concatenate라서.) 숫자를 문자로 변환해야 함.
print()

# Identity
temp = c    # 깊은 복사
print(id(temp))
print(id(c))
print(c.remove(85))
print(temp)
print()

# 수정, 삭제
c[0] = 0
print(c)
c[1] = 1,2,3
print(c)
c[2:3] = 'abc'   # 요소를 한꺼번에 대체. 길이는 달라도 관계없음(튜플과 문자열, 리스트 모두 iterable 객체이므로 가능함)
print(c)
del c[2]
print(c)

# 리스트 함수
a = [5,2,3,1,4]