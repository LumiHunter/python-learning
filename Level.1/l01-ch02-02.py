# 기본 선언
n = 70
# n에 값을 할당했다: 메모리(저장장치)에 n의 주소를 마련하고 해당 주소에 값을 할당한다.

# 동시 선언
x = y = z = 700

# 재선언: var의 주소에 다른 값을 할당함.
var = 75
var = 'Change Value'

# Object References: 변수에 값이 할당 상태일 때,
n = 777
print(n, type(n))
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력(호출)

# id 확인: 객체의 고유값 확인
m = n
print(id(m) == id(n))
a = 777
b = 777
print(id(a) == id(b))
print(id(m) == id(n) == id(a) == id(b))
# 보기에는 4개의 변수를 선언했지만 '같은 값'이기 때문에,
# 파이썬 인터프리터는 이름이 다른 변수에 같은 값이 할당될 때
# 하나의 오브젝트를 참조하도록 한다.
# 만약 변수에 연산 등을 거쳐 변경이 생기면 그때 새로운 오브젝트를 생성한다.

# Camel Case: numberOfCollegeGraduates -> Method
# Pascal Case: NumberOfCollegeGraduates -> Class
# Snake Case: number_of_college_gruadutes


