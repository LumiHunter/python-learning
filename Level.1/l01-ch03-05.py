# 딕셔너리 자료형 -> 순서O (키)중복X 수정O 삭제O

a = {}
b = {
    'Name': 'Niceman', 
    'City': 'Seoul', 
    'Age': 33
    }
c = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33)
])
d = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
)

# print(b['Phone']) 
print(b.get('Phone'))    # 없는 키에 대해서는 KeyError가 발생. get 함수로 호출하면 None 처리

d['Phone'] = '01012345678'
print(d)
print(len(d))

# 딕셔너리 함수: dict_keys, dict_values, dict_items -> 객체들이므로, 편히 보기위해선 list로 변경해야
print(d.keys())
print(d.values())
print(d.items())
print(list(d.items()))

print(d.pop('Phone'))
print(d)
print(d.popitem())    # '무작위로' pop -> 딕셔너리는 순서가 없으므로.
print(d)
print()

print('City' in d)    # Key가 있는지 조회
print()

# 수정 & 추가 함수 update
d.update(City='Gyeongki')
print(d)
temp = {'Age': 27, 'Phone': '01012345678'}    # 다른 딕셔너리를 추가 가능
d.update(temp)
print(d)