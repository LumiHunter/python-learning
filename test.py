# 파이썬 모듈
# Module: 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

if __name__ == '__main__':    # 해당 모듈이 외부에서 호출될 때 이 if절 안의 코드는 실행되지 않는다.
    print('inner called')
    