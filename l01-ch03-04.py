# 튜플 자료형 -> 순서O 중복O 수정X 삭제X: immutable -> 중요한 데이터, 절대 변하면 안되는 값.

a = ()
b = (1)    # integer로 인식됨
c = (1,)    # 콤마로 끝나야 튜플
d = (100, 1000, 'a', 'b', 'c')
e = 70, 75, 80, 85
f = (100, 100.1, ['Ace', 'Base', 'Captine'])
g = (21.42, 'foobar', 3, 4, False, 3.14159)

print(c + d)
print(c * 3)

# 튜플 함수 -> 수정, 삭제가 불가하므로 index, count 정도
a = (5,2,3,1,4)
print(a.index(3))
print(a.count(1))

# Packing & Unpacking
t = ('foo', 'bar', 'buzz')    # 여러 원소를 한데 묶어 인덱스로 접근할 수 있게 함 -> 팩킹

(x1, x2, x3) = t    # 반대로, 팩킹되어 있는 원소를 각각의 변수에 할당함 -> 언팩킹
print(x1, x2, x3)
print(type(x1), type(x2), type(x3))