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

# 문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Gwangju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)    # 시퀀스형들은 in을 쓸 수가 있다.
print('P' not in str_o2)
print()

# 문자열 함수 -> 너무 많으니 검색해야.
print(str_o1.capitalize())    # 시작 글자를 대문자로
print(str_o2.endswith('s'), str_o2.startswith('a'))    # 마지막/첫번째 문자 체크
print(str_o3.replace('are', 'was'))
print(str_o4.split(' '))
print(str_o1.join(["I love ", "!"]))    # 앞, 뒤에 문자 추가: join, [앞, 뒤]로 변수 넣어야 함.
print(sorted(str_o2))    # ABC 순으로 정렬 -> 리스트
print(sorted(str_o2, reverse=True))    # 역순으로 정렬
print(reversed(str_o2))    # 거꾸로 쓰기(정렬X) -> 객체이므로 list 형태로 변환해줘야 함
print(list(reversed(str_o2)))
print()

# 반복(시퀀스)
im_str = "Good boy"
print(dir(im_str))    # 네임스페이스에 __iter__ 가 있는 객체는 '반복 가능'

# 슬라이싱
str_sl = "Nice Python"
print(str_sl[1:4:2])
print(str_sl[::-1])
print()

# 아스키코드
a = 'z'
print(ord(a))    # 문자 -> 아스키코드
print(chr(65))    # 아스키코드 -> 문자