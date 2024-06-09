# while <expr>:
#   <statement(s)>

n = 5
while n > 0:
    print(n)
    n -= 1

a = ['foo', 'bar', 'baz']
print()

while a:
    print(a.pop())
print()

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended')
print()

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop ended')
print()

i = 10
while i > 0:
    i -= 1
    print(i)
    if i == 5:
        break
else:
    print('else out.')    # while이 다 돌면->break나 return으로 종료되지 않으면
print()

a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'
i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list')
print()

a = ['foo', 'bar', 'baz']
while True:
    if not a:    # 무한반복되는 while True라도 break처리하는 경우도 많음
        break
    print(a.pop())