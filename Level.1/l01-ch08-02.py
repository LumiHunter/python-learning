# External 함수
# sys, pickle, shutil, temfile, time, random

import sys
print(sys.argv)    # 현재 경로(와 인자)
# sys.exit()    강제종료
print(sys.path)    # 파이썬 패키지 위치

# # 객체 파일 쓰기: 파이썬에서 쓰는 데이터타입을 파일로 쓸 때.
import pickle
f = open('test.obj', 'wb')
obj = {1: 'python', 2: 'javascript', 3: 'C'}
pickle.dump(obj, f)
f.close()

f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

# 환경변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
import os
print(os.environ)    # 딕셔너리 형으로 환경변수
print(os.environ['USERNAME'])
print(os.getcwd())

import time
print(time.time())
print(time.localtime(time.time()))
print(time.ctime())    # 간단히 형 변환
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))    # 형식 표현
for i in range(5):
    print(i)
    time.sleep(1)

import random
print(random.random())    # 0~1 실수
print(random.randint(1,45))    # 주어진 간격 안에서 랜덤 정수(1,45)
print(random.randrange(1,44))    # range 함수의 응용(1~44)
d = [1,2,3,4,5]
random.shuffle(d)    # 섞기
print(d)
c = random.choice(d)    # 무작위 선택

import webbrowser     # 웹 브라우저 실행시키기
webbrowser.open('http://google.com')
webbrowser.open_new('http://google.com')    # 새 창으로