# 파이썬의 핵심 -> 시퀀스, 반복, 함수, 클래스(Sequence, Iterator, Functions, Class)
# 스페셜 메소드(매직 메소드): 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드(Low level)

class Vector():
    def __init__(self, *args):
        '''Create a vector, example : v = Vector(5, 10)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
    
    def __repr__(self):
        '''Return the vector informations.'''
        return 'Vector (%r, %r)' % (self._x, self._y)
    
    def __add__(self, other):
        '''Return the vector addition of self and the other.'''
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)
    
    def __bool__(self):
        return bool(max(self._x, self._y))
    
print(Vector.__init__.__doc__)
v1 = Vector(5,7)
v2 = Vector(23, 37)
v3 = Vector()

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(bool(v1), bool(v3))