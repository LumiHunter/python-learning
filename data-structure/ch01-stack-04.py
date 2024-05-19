# 스택을 리스트로 대체해서 쓰기
# 리스트-스택 이용 예시: 문자열 역순 출력

stack_list = []
s = input('문자열 입력: ')

for c in s:
    stack_list.append(c)
    
print('문자열 출력: ', end='')
while len(stack_list) != 0:
    print(stack_list.pop(), end='')
print()

# 스택을 만들어주는 queue 모듈: queue의 LifoQueue
# push(), pop() -> put(), get()
# isEmpty(), isFull() -> empty(), full()
# peek() -> 없음

import queue
stack = queue.LifoQueue(maxsize=100)
msg = input('문자열 입력: ')

for c in msg:
    stack.put(c)

print('문자열 출력: ', end='')
while not stack.empty():
    print(stack.get(), end='')
print()