# 읽기 r, 쓰기 w, 추가 a, 텍스트 t, 바이너리 b
# (상대경로) '../': 상위 './': 현재 -> 현재경로는 '터미널'의 위치. 현재 작업중인 .py 파일의 위치가 아님!!

f = open('./Level.1/resource/it_news.txt', 'r', encoding='UTF-8')    # t: 텍스트가 디폴트이므로 'rt'가 아니라 'r', 바이너리로 읽는다면 'rb'
# 파일을 열어보면 VS Code 우측 하단에 encoding이 명시되어 있음.
# open의 encoding 디폴트는 UTF-8
print(dir(f))
print(f.encoding)
print(f.name)
print(f.mode)
cts = f.read()
print(cts)
f.close()    # 반드시 close
print()

# with문
with open('./Level.1/resource/it_news.txt', 'r', encoding='UTF-8') as f:    # 저절로 close해줌
    c = f.read()
    print(c)
    print(iter(c))    # str_iterator object이므로 반복가능.
    print(list(c))
print()

# 특정 글자수만큼 읽기
with open('./Level.1/resource/it_news.txt', 'r', encoding='UTF-8') as f:    # 저절로 close해줌
    c = f.read(20)    # 20Byte 만큼만 읽어옴!
    print(c)
    c = f.read(20)    
    print(c)
    c = f.read(20)    # 내부적으로 '커서'가 작동하므로, 이전 read에서 어디까지 읽었는지 기억하고 그 다음부터 읽기 시작함.
    print(c)
    f.seek(0,0)   
    c = f.read(20)
    print(c)
print()

# 한 줄 씩 읽기
with open('./Level.1/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)

# 전체를 읽은 후 line 단위로 list 저장하기 -> 줄 단위를 리스트로 바꿔주기
with open('./Level.1/resource/it_news.txt', 'r', encoding='UTF-8') as f: 
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

# 파일 쓰기
with open('./Level.1/contents1.txt', 'w') as f: 
    f.write('I love python\n')

# 기존 파일에 덮어 쓰기 -> 같은 경로에 그대로
with open('./Level.1/contents1.txt', 'w') as f: 
    f.write('I love python2\n')

# 기존 파일에 이어 쓰기 -> append
with open('./Level.1/contents1.txt', 'a') as f: 
    f.write('I love python3\n')

# 리스트 -> 파일
with open('./Level.1/contents2.txt', 'w') as f: 
    list = ['Orange\n', 'Apple\t', 'Banana', 'Melon']
    f.writelines(list)    # 줄바꿈 \n, 탭 \t 등을 리스트에 넣어주지 않으면 그대로 붙여 이어 씀!

# 콘솔이 아닌 파일로 출력하기
with open('./Level.1/contents3 .txt', 'w') as f: 
    print('Test Text Write', file=f)

with open('./Level.1/contents4 .txt', 'w') as f:     # 아무것도 입력하지 않아도 파일은 생성됨.
    print(type(f))    # <class '_io.TextIOWrapper'>