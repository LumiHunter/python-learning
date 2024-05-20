import sys
print(sys.path)     # 파이썬 내부적으로 쓰는 built-in 모듈 sys로 모듈, 패키지들이 어디있는지 검색
print(type(sys.path))    # 리스트

# sys.path.append('추가하고자 하는 경로')
# sys.path에 현재 폴더는 defalut로 추가되어 있다

import test
print(test.add(1, 2))