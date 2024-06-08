# for in <collection>
#   <loop body>

for v1 in range(10):
    print('v1 is ', v1)
    
for v2 in range(1, 11):
    print('v2 is ', v2)
    
for v3 in range(1, 11, 2):
    print('v3 is ', v3)
    
result = 0
for i in range(1,1001):
    result += i
print(result)
print(sum(range(1,1001)))    # sum 함수
print(type(range(1,1001)))    # range라는 iterator
print()
# iterables 자료형: 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip -> ch08-1 참조

names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print('You are', name)
print()

word = 'beautiful'
for s in word:
    print(s)
print()

my_info = {
    'name': 'Lee',
    'Age': 33,
    'City': 'Seoul'
}

for k in my_info:
    print(k, 'is', my_info.get(k))
for k in my_info.values():
    print(k)
for key, value in my_info.items():
    print(key, ':', value)
print()

name = 'fineAppLE'
for n in name:
    if n.isupper():    # 대문자인지 확인
        print(n)
    else:
        print(n.upper())
print()

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found ', 34)
        break
print()

lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:    # is는 '자료형'을 검사할 때
        continue
    print('Current type:', type(v))
    print('multiply by 2', v*2)
print()

# for-else
# 모든 원소를 다 반복했을 때(break를 만나거나 return을 하여 도중에 끝나지 않았을 때) else문 실행
for num in numbers:
    if num == 49:
        print('Found: 24')
        break
else:
    print('Not Found: 24')
print()

for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i * j), end='')    # 4자리의 정수형! 간격이 일정해진다
    print()

name2 = 'Aceman'
print('Reversed', reversed(name2))
print('Reversed list', list(reversed(name2)))
print('Reversed Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))    # 순서가 없어 revered 의미 없음!
