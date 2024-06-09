# input()의 기본 타입: str

name = input('Enter your name: ')
grade = input('Enter your grade: ')
company = input('Enter your company name: ')

print(name, grade, company)

first_number = int(input('Enter number 1: '))
second_number = int(input('Enter number 2: '))
print('first number + second number =', first_number + second_number)

# print 안에서 바로 input 사용: 변수 선언하지 않는 대신 input으로 바로 사용.
print('First Name: {0}, Last Name: {1}'.format(input('Enter first name: '), input('Enter second name: ')))

# 예외처리 -> 사용자에게 원하는 자료형을 요구
try:
    n = int(input('Enter a number: '))
    print('OK, Your number is:', n)
except ValueError:
    print('This is not a number.')
    
# while -> 올바른 값 입력할 때까지 반복
while True:
    try:
        n = int(input('Enter a number: '))
        print('OK, Your number is:', n)
        break
    except ValueError:
        print('This is not a number.')
        
    
