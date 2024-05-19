from Structures.stack import ArrayStack

# 스택 이용 예시: 괄호검사 알고리즘
def checkBrackets(input_statement):
    stack = ArrayStack(100)
    for c in input_statement:
        if c in ['(', '[', '{']:
            stack.push(c)
        elif c in [')', ']', '}']:
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if left + c not in ['()', '[]', '{}']:
                    return False
    return stack.isEmpty()

input_statement = input('100 이하의 문자열: ')
print(checkBrackets(input_statement))
