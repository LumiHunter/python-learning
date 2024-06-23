# 시퀀스형에는 두 가지 종류가 있다.

# 컨테이너(Container): 서로 다른 자료형 -> 리스트, 튜플, collections.deque
# 플랫(Flat): 한 개의 자료형 -> 문자열(str), bytes, bytearray, array.array, memoryview

# 가변형(mutable): 리스트, 집합, 딕셔너리, bytearray, array.array, memoryview, collections.deque
# 불변형(immutable): 튜플, 문자열(str), bool, int, float, bytes, frozenset

# 해시테이블 -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X
# Set -> 중복 허용 X

# immutable Dict
from types import MappingProxyType
d = {'key1': 'value1'}

# Read Only화: d는 수정 가능, d_frozen은 수정 불가
d_frozen  = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
try:
    print(hash(d))
    print(hash(d_frozen))
except TypeError:
    print('d and d_frozen both are not hashable.')
    
d['key2'] = 'value2'
# d_frozen['key2'] = 'value2' 수정 불가
print()

s1 = {'Apple', 'Orange', 'Apple', 'Kiwi', 'Tomato'}
s2 = set(['Apple', 'Orange', 'Apple', 'Kiwi', 'Tomato'])
s3 = {3}
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Kiwi', 'Tomato'})    # Readonly
s1.add('Melon')
print(s1)
try:
    s5.add('Melon')
except AttributeError:
    print("frozenset object has no attribute 'add'")
print()

# 선언 최적화
# 파이썬: 바이트 코드 -> assembling 후 파이썬 인터프리터가 byte 코드를 실행

from dis import dis    # dis: byte 코드가 어떻게 생성되는 지 순서를 볼 수 있음
print('-------')
print(dis('{10}'))    # 실행 과정이 더 적음 -> 조금이나마 더 빠른, 최적화된 선언
print('-------')
print(dis('set([10])'))
print()

# Comprehending Set
from unicodedata import name
print({name(chr(i), '') for i in range(0,256)})