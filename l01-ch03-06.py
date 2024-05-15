# 집합 자료형 -> 순서X 중복X 추가O 삭제O

a = {}    # 이건 딕셔너리!
b = set()
c = set([1,2,3,4])    # 리스트 형태로 넣어야 함

print(3 in c)
print(len(c))
print()

# 튜플/리스트 변환 -> 집합 자체를 변환하는 것이 아님
print(type(tuple(c)))
print(type(c))
print(type(list(c)))
print(c)
print()

# 집합 연산
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1-s2)
print(s1.difference(s2))
print(s1.isdisjoint(s2))    # disjoint: 서로소
print(s1.issubset(s2))
print(s1.issuperset(s2))
print()

# 추가, 제거-> 집합을 직접 변화시킴
s3 = set([1,2,3,4])
s3.add(5)    # append가 아님!!
s3.remove(2)
print(s3)
print(s3.discard(2))    # 없는 것을 지우려고 해도 KeyError 발생하지 않음
print(s3)
s3.clear()
print(s3)