x = 50
y = 100
text = 308276567
n = 'lee'

ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)

ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n = n, s = text, sum = x+y)
print(ex2)

# f-string
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)

# 천단위 구분 기호
m = 1000000000000000
print(f'{m:,}')

# 정렬
t = 20
print(f'{t:^10}')    # 가운데 정렬, 가운데
print(f'{t:>10}')
print(f'{t:<10}')
print(f'{t:-^10}')    # 빈공간 '-' 채우기
print(f'{t:#>10}')
print(f'{t:%<10}')