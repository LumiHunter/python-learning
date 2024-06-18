# 시퀀스형에는 두 가지 종류가 있다.

# 컨테이너(Container): 서로 다른 자료형 -> 리스트, 튜플, collections.deque
# 플랫(Flat): 한 개의 자료형 -> 문자열(str), bytes, bytearray, array.array, memoryview

# 가변형(mutable): 리스트, 집합, 딕셔너리, bytearray, array.array, memoryview, collections.deque
# 불변형(immutable): 튜플, 문자열(str), bool, int, float, bytes, frozenset

# Tuple Advanced
# Unpacking

print(divmod(100,9))
print(divmod(*(100,9)))    # divmod에 (100,9)를 인자로 주는 것이 아니라 언패킹을 해서 100,9를 줌.
print(*(divmod(100,9)))    
print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1,2,3,4,5
print(x, y, rest)

# mutable(가변) vs immutable(불변)
l = (15,20,25)
m = [15,20,25]
print(id(l), id(m))
l = l * 2
m = m * 2
print(id(l), id(m))    # '재할당' 하는 것이므로 둘 모두 id가 바뀜
l *= 2
m *= 2
print(id(l), id(m))    # '변경'하는 것이므로 mutable한 리스트는 id를 유지하는 반면 immutable한 튜플은 새 id에 할당해버림!

# sort vs sorted
# reverse, key=len, key=str.Lower, key=func...
# sorted: 정렬 후 새로운 객체 반환(원본 수정 X)
# sort: 정렬 후 객체 직접 변경(원본 수정 O)

f_list = ['orange', 'apple', 'melon', 'mango', 'banana', 'grape', 'strawberry', 'papaya', 'lemon']
print(sorted(f_list))
print(sorted(f_list, reverse=True))    # 역순
print(sorted(f_list, key=len))    # 길이 순
print(sorted(f_list, key=lambda x: x[-1]))    # 마지막 글자 순
print(sorted(f_list, key=lambda x: x[-1], reverse=True))
print(f_list)

print(f_list.sort(), f_list)    # 반환값은 None -> 원본이 수정되었으므로
print(f_list.sort(reverse=True), f_list)    # 반환값은 None -> 원본이 수정되었으므로
print(f_list.sort(key=len), f_list)
print(f_list.sort(key=lambda x: x[-1]), f_list)
print(f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# 리스트 vs array
# 융통성, 다양한 자료형, 범용적 사용 -> 리스트
# 숫자 기반 -> 배열(array), 단 리스트와 거의 호환됨.