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

# next 패턴
class WordSplitter():
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)
    
wi = WordSplitter('Do today what you could do tommorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가하면 메모리 사용량 증가 -> 제네레이터 사용을 권장함
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator():
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        print('Called __iter__')
        for word in self._text:
            yield word     # 제네레이터!! 인덱스를 명시하지 않아도 내부적으로 다음에 반환될 값에 대한 상태를 기억하고 있다!
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tommorrow')
wt = iter(wg)
print(wg)
print(wt)
print(next(wt))
print(next(wt))    # yield 키워드에서 나가지 않기 때문에, 'Called __iter__'는 다시 출력되지 않는다!
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))    # StopIteration 예외 발생
