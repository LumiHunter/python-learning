#빈 문자열
str_t1 = ''
str_t2 = str()

# 이스케이프 문자 사용
print("I'm boy.")
print("I\'m boy.")
print('a \t b')
print('a \n b')
print('a \000 b')    # NULL

print()
# Raw String: 경로 지정하는 슬래시 기호를 사용하기 위해 이스케이프 문자를 무시!
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티라인 입력
# 역슬래시를 사용해 코드를 여러줄로 나눠 쓸 수 있다.
multi_str = \
'''
String
Multi line
Test
'''

print(multi_str)

print()

# 문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Gwangju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)    # 시퀀스형들은 in을 쓸 수가 있다.
print('P' not in str_o2)