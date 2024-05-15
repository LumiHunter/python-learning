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
print(a.index(1), a[1])    # 인덱스로 불러오는 방법 두가지
print(a)
a.append(10)    # a 리스트 자체를 변경함
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.insert(2,7)    # (인덱스 번호, 넣고자 하는 요소)
print(a)
a.remove(10)
print(a)
print(a.pop())    # 마지막 인덱스에 있는 원소를 return하면서 리스트에서 제거
print(a)
print(a.count(2))
ex1 = [8,9]
a.extend(ex1)    # iterable 객체를 뒤에 이을 때
print(a)
ex2 = '89'
a.extend(ex2)    
print(a)
ex3 = 8,9
a.extend(ex3)
print(a)

while a:    # 빈 리스트: False
    print(a.pop())