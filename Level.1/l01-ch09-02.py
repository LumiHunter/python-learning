# CSV: MEME - text/csv

import csv

with open('./Level.1/resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)    # 커서 하나 넘김: 헤더 스킵 -> pop() 처럼 return 하므로, 하나씩 출력할 때 사용하기도 함.
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)    # 리스트
        print(': '.join(c))    # 문자열 함수 -> ch03-02 참조: ' ' 앞, 뒤에 문자 추가

with open('./Level.1/resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')    # 지정된 분할 문자(default는 ,)
    for c in reader:
        print(c)

with open('./Level.1/resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)    # 자동으로 header가 key가 됨!
    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('--------------')

w = [[1,2,3], [4,5,6], [7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./Level.1/write1.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f, lineterminator='\r')    # 한 줄 처리 후 한 칸만 띄우는 옵션
    print(type(wt))
    print(dir(wt))

    for v in w:
        wt.writerow(v)     # 하나의 리스트가 하나의 레코드

with open('./Level.1/write2.csv', 'w', encoding='utf-8') as f:
    fields = ['One', 'Two', 'Three']
    wt = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')    # lineterminator의 default는 \r\n 인데, \r은 '출력 위치를 줄 맨 앞으로 옮기는 것' 이므로 두번 엔터를 친 셈이 된다.
    wt.writeheader()    # 헤더 작성
    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})