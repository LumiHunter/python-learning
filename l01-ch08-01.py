# Built-in 함수

# 절대값
print(abs(-3))

# interable 요소 검사: 0은 False임. True 검사
print(all([1,2,3])) # and 
print(any([1,2,0])) # or

# 아스키 <-> 문자
print(chr(67))
print(ord('C'))

# enumerate: 인덱스 + iterable 객체 생성
for i, name in enumerate(['a', 'b', 'c']):
    print(i, name)
print()

# filter: 반복가능한 객체요소를 지정한 함수 조건에 맞는 값만 추출
def conv_pos(x):    # True / False만 나오는 조건식 함수!
    return abs(x) > 2

print(list(filter(conv_pos, [1,2,-3,4,5])))
print(list(filter(lambda x: abs(x) > 2, [1,2,-3,4,5])))

# map: 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-2,3,-4,5])))
print(list(map(lambda x: abs(x), [1,-2,3,-4,5])))