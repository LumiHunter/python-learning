import sys
print(sys.path)     # 파이썬 내부적으로 쓰는 built-in 모듈 sys로 모듈, 패키지들이 어디있는지 검색
print(type(sys.path))    # 리스트

# sys.path.append('C:\\Users\\hwang\\learning\\Inflearn\\python-ex\\python-learning\\test-modules')

import test
print(test.add(1, 2))