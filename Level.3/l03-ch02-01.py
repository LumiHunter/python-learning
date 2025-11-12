'''
Context Manager Annotation
Keyword - @contextlib.contextmanager, __enter__, __exit__
'''
'''
Contextlib 데코레이터 사용: 코드가 직관적, 예외 처리 용이성
'''

# Using decorator
import contextlib
import time

@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f     # __enter__
    f.close()    # __exit__
    
with my_file_writer('testfile4.txt', 'w') as f:
    f.write('Context Manager Test4\nContextlib Test4')

@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try:    # __enter__
        yield start
    except BaseException as e:
        print('Logging exception: {}: {}'.format(msg, e))
        raise
    else:     # __exit__
        print('{}: {} s'.format(msg, time.monotonic() - start))
        
with ExcuteTimerDc('Job started') as v:
    print('Received start monotonic2: {}'.format(v))
    n = 0
    for i in range(10000000):
        n+=i 
    #raise ValueError('Raise Exception')   # 예외 발생시키기 