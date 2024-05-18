# 스택을 위한 데이터: capacity, array, top
capacity = 10
array = [None] * capacity    # capacity만큼 '빈 공간'을 구현
top = -1

# 스택의 공백 상태와 포화 상태 검사
def isEmpty():
    return top == -1

def isFull():
    return top == capacity

# 스택의 push()
def push(e):
    # global top이 있는 경우임!
    if isFull():
        print('Stack overflow')
        exit()    # 코드 강제 종료
    top += 1
    array[top] = e
    
# 스택의 pop()
def pop():
    if isEmpty():
        print('Stack underflow')
        exit()
    top -= 1
    return array[top+1]

# 스택의 peak()
def peak():
    if isEmpty():
        print('Stack underflow')
        exit()
    return array[top]

# 스택의 size()
def size():
    return top+1    # capacity만큼 채워져있는 리스트이므로 len()을 쓸 수 없음

