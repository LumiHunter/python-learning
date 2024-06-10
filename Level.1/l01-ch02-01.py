# print separator 옵션 사용
print('P', 'Y', 'T', 'H','O','N')    # default: ' '
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')
print()

# print end 옵션 사용
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Site')    # default: \n

print()

# file 옵션: print 내용을 파일로 저장
import sys
print('Learn Python', file=sys.stdout)    # sys.stdout: 현재 콘솔
print()

# format 사용(d:정수, s:문자열, f:실수)
print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))    # 인덱스 지정
print()

# %s
print('%10s' % ('nice'))    # 10자리수 확보(오른쪽 정렬)
print('{:>10}'.format('nice'))    # 왼쪽부터 공백으로 채운 다음 원하는 문자열을 출력함

print('%-10s' % ('nice'))    # 10자리수 확보(왼쪽 정렬)
print('{:10}'.format('nice'))     # 오른쪽부터 공백으로 채운 다음 원하는 문자열을 출력함

print('{:#>10}'.format('nice'))   # 공백 대신 채울 문자 지정 가능

print('{:^10}'.format('nice'))   # 중앙 정렬!

print('%5s' % ('python'))
print('%.5s' % ('python'))    # 자리수 확보한 이상이면 절삭
print('{:>10.5}'.format('python'))    # 10자리 확보, 5개만 출력
print('{:10.5}'.format('python'))
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))    # 오른쪽 정렬
print('{:>4d}'.format(42))    # d를 생략하면 안됨
print('%-4d' % (42))    # 왼쪽 정렬
print('{:4d}'.format(42))    # format으로 d는 오른쪽 정렬만
print('{:#>4d}'.format(42))
print()

# %f
print('%f' % (3.14159265358979323846))    # defalut 소수부 6자리까지
print('%1.8f' % (3.14159265358979323846))    # 정수부.소수부 자리수 지정
print('%06.2f' % (3.14159265358979323846))    # '총' 6자리 확보, 정수부에 0으로 채움.

print('{:f}'.format(3.14159265358979323846))    # defalut 소수부 6자리까지
print('{:06.2f}'.format(3.14159265358979323846))