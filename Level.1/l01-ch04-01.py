print(type(True))    # 0이 아닌 수, "abc", [1,2,3...], (1,2,3...) ...
print(type(False))    # 0, "", [], (), {}

# 관계연산자: >, <, >=, >=, ==, !=
# 논리연산자: and, or, not

a, b, c = 75, 40, 50

print('and: ', a > b and b > c)
print('or: ', a > b or b > c)    # or 연산은 앞이 True면 뒤는 실행하지 않음
print('not: ', not a > b)
print()

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1: ', 3+12 > 7+3)
print('e2: ', 5+10*3 > 7+3*20)
print('e3: ', 5+10 > 3 and 7+3 == 10)
print('e4: ', 5+10 > 0 and not 7+3 == 10)
print()

score1 = 90
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')
print()

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
# 한글 print 깨짐 방지

id1 = 'vip'
id2 = 'admin',
grade = 'platinum'
if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')
elif id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')
print()

grade = 'A'
total = 95
if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')
print()

q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name": "Lee", "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print("name" in e)    # 딕셔너리는 키로 조회
print("Seoul" in e.values())    # 값을 조회하고자 하면 values() 메소드
print(13 not in r)