# 시퀀스형에는 두 가지 종류가 있다.

# 컨테이너(Container): 서로 다른 자료형 -> 리스트, 튜플, collections.deque
# 플랫(Flat): 한 개의 자료형 -> 문자열(str), bytes, bytearray, array.array, memoryview

# 가변형(mutable): 리스트, 집합, 딕셔너리, bytearray, array.array, memoryview, collections.deque
# 불변형(immutable): 튜플, 문자열(str), bool, int, float, bytes, frozenset

# 해시테이블: key에 value를 저장하는 구조
# 파이썬 dict 해시테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조

# Hash 값을 확인 -> 고유한 값
t1 = (10, 20, 30, 40, 50)    # 불변형으로만 이루어져 있으므로 hash 가능
t2 = (10, 20, [30, 40, 50])  # mutable한 리스트가 들어있으므로 hash 불가

print(hash(t1)) 
# print(hash(t2)) 
print()

source = (('k1', 'val1'), 
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'),)

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
        
print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)

# 주의
new_dict3 = {k: v for k,v in source}
print(new_dict3)     # 나중 값으로 덮어 써버림!