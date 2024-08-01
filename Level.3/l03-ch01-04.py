'''
Context Manager
Keyword - Contextlib, __enter__, __exit__, exception
'''
'''
컨텍스트 매니저: 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
가장 대표적인 with 구문 이해
정확한 이해 후 사용, 프로그래밍 개발에 중요
'''
'''
Contextlib = Measure execution 제작
'''

# originally
file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1\nContextlib Test1')
finally:
    file.close()

# with 구문 등장
with open('./testfile2.txt', 'w') as f:
    f.write('Context Manager Test2\nContextlib Test2')

# Use Class -> Context Manager(__) with exception handling
class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started: __init__')
        self.file_obj = open(file_name, method)
    
    def __enter__(self):    # 내부적으로 원하는 기능 달면, with를 붙여 사용 시 원하는 기능 구현 가능
        print('MyFileWriter started: __enter__')
        return self.file_obj
    
    def __exit__(self, exc_type, value, trace_back):    
        # 예외가 발생했을 때 예외 타입/예의 값/트레이스 백
        # __exit__는 인자 셋의 역할이 위와 같이 정해져있다.
        print('MyFileWriter started: __exit__')
        if exc_type: 
            print('Logging exception {}'.format((exc_type, value, trace_back)))
        self.file_obj.close()

with MyFileWriter('./testfile3.txt', 'w') as f:
    f.write('Context Manager Test3\nContextlib Test3')


import time

class ExcuteTimer():
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print('Logging exception {}'.format((exc_type, exc_value, exc_traceback)))
        else:
            print('{} {} s'.format(self._msg, time.monotonic() - self._start))
        return True
    

with ExcuteTimer('Excuting job') as v:
    print('Received start monotonic1: {}'.format(v))
    # Excute job
    n = 0
    for i in range(10000000):
        n+=i
    raise Exception('Raise Exception')   # 예외 발생시키기    