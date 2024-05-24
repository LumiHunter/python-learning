# External 함수
# sys, pickle, shutil, temfile, time, random

import sys
print(sys.argv)    # 현재 경로(와 인자)
# sys.exit()    강제종료
print(sys.path)    # 파이썬 패키지 위치

# 객체 파일 쓰기: 파이썬에서 쓰는 데이터타입을 파일로 쓸 때.
import pickle
f = open('test.obj', 'wb')
obj = {1: 'python', 2: 'javascript', 3: 'C'}
pickle.dump(obj, f)
f.close()

f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()