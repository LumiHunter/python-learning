# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 
# -> '어디까지 했는지 마지막 시점을 기억하는 것': 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 
# -> '동시에 수행한 다음 수합하는 것' : 속도

# Generator ex1
def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')    # 이 아래로 yield - 작동 동작이 없기 때문에 'StopIteration' 발생

temp = iter(generator_ex1())
print(next(temp))
print(next(temp))
# print(next(temp))
print()

for v in generator_ex1():    # for문은 StopIteration에 대한 예외처리도 구현되어 있음
    print(v)
print()

# Generator ex2
temp2 = [x * 3 for x in generator_ex1()]    
# 리스트 컴프리헨션으로 generator_ex1은 세 번 호출.
# 호출 될 때마다 yield까지 실행되기 때문에, 
# 'Start'를 출력하고 x에 'A Point'를 반환하고
# 'Continue'를 출력하고 x에 'B Point'를 반환하고
# 'End'를 출력하고 x에 반환할 값이 없어 for문이 종료됨.
print(temp2)
for i in temp2:
    print(i)
print()

temp3 = (x * 3 for x in generator_ex1())
# 제네레이터이므로, temp3를 선언하는 것만으로는 아직 generator_ex1이 호출되지 않음
print(temp3)
for i in temp3:
    # temp3가 iter로 실행될 때 generator_ex1 호출, i에 x * 3을 반환
    # 'Start'를 출력하고 i에 'A PointA PointA Point'를 반환하고
    # 'Continue'를 출력하고 i에 'B PointB PointB Point'를 반환하고
    # 'End'를 출력하고 i에 반환할 값이 없어 for문이 종료됨.
    print(i)
print()

# Generator ex3
# 중요 함수: filterfalse, accumulate, chain, product, groupby...

import itertools
gen1 = itertools.count(1, 2.5)    # 1부터 2.5씩 늘리기 -> 무한대로!
print(gen1)
print(dir(gen1))    # __iter__와 __next__ 존재
print(next(gen1))
print()

gen2 = itertools.takewhile(lambda n : n < 10, gen1)    # iter를 주어진 조건(lambda 함수)를 충족할 때까지만 제한
# 주의: 위에서 gen1의 next를 한번 호출했으므로, 
# n은 1부터 시작하지 않고 다음 값인 3.5부터 시작한다!
for v in gen2:
    print(v)

gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])    # 반대로 필터
for v in gen3:
    print(v)

gen4 = itertools.accumulate([x for x in range(1, 11)])    # 누적 합계
for v in gen4:
    print(v)

gen5 = itertools.chain('ABCDE', range(1,11,2))    # 연결
print(list(gen5))
print(list(gen5))    # 주의: 이 모든 itertools들은 generator로서, 한번 다 돌아가고 나면 더 이상 반환할 값이 없다!

gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

gen7 = itertools.product('ABCDE')
print(list(gen7))

gen8 = itertools.product('ABCDE', repeat=3)    # 경우의 수 연산!(중복순열)
print(list(gen8))

gen9 = itertools.groupby('AAAABBBCCCCDDEEEEEE')    # 그룹화
for chr, group in gen9:
    print(chr, ':', list(group))