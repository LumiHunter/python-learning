# 여러개의 '스택' 자료구조를 찍어내어 사용할 수 있도록 -> 클래스 화!

class ArrayStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1
        
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity-1
    
    def push(self, item):
        if self.isFull():
            print('Stack overflow')
            exit()
        self.top += 1
        self.array[self.top] = item
    
    def pop(self):
        if self.isEmpty():
            print('Stack underflow')
            exit()
        self.top -= 1
        return self.array[self.top+1]
    
    def peak(self):
        if self.isEmpty():
            print('Stack underflow')
            exit()
        return self.array[self.top]
    
    def size(self):
        return self.top+1
    
    def clear(self):
        while self.top != -1:
            self.array[self.top] = None
            self.top -= 1
            
    def display(self):
        for i in range(self.top):
            print(self.array[i], end=' ')

# 스택 이용 예시: 문자열 역순 출력    
s = ArrayStack(100)
msg = input("sequence input: ")
for c in msg:
    s.push(c)
    
print("reverse print: ", end='')
while not s.isEmpty():
    print(s.pop(), end='')
print()