# 병행성(Concurrency)
# Iterator, Generator

# 파이썬에서 반복 가능한(interable) 타입: collections, text, list, Dict, Set, Tuple, unpacking, *args....

# 반복 가능한 이유> -> t가 내장한 iter(x) 함수가 호출되었기 때문에.
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for c in t:
#     print(c)

w = iter(t)
print(dir(w))    # next 존재

print(next(w))
print(next(w))

while True:
    try:
        print(next(w))
    except StopIteration:
        break
# 이것이 for문의 내부적 원리!

# 반복형 확인
print(dir(t))
print(hasattr(t, '__iter__'))    # attribute를 가지고 있는지 확인하는 함수 hasattr

from collections import abc    # abc: abstract class의 약자.
print(isinstance(t, abc.Iterable))    # 추상클래스-Iterable을 상속받은 객체가 맞는지 확인.
print()

# next
class WordSplitter():
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')