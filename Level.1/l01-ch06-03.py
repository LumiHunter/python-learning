# 파이썬 패키지: 모듈들이 모여있는 폴더
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성된다!
# 상대경로: ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용
# __init__.py: Python 3.3부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천. (과거에는 빈 __init__.py가 있어야 인식 가능했음)
# __init__.py의 __all__ = [파일이름 리스트] 로 외부에서 import할 수 있는 것을 제한해줄 수 있음.

import sub.sub1.module1
import sub.sub2.module2

sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()

from sub.sub1 import module1
from sub.sub2 import module2 as m2   # alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()

from sub.sub1 import *    # 권장되지 않음. 사용할 것만 가져오는 것이 성능하락(메모리 누수)을 예방할 수 있음
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module1.mod1_test1()
module2.mod2_test2()

print()

from sub.sub3 import module3 as m3
print(m3.add(2,5))
print(m3.power(2,10))