'''
keyword: Shallow Copy & Deep Copy
'''
'''
객체의 복사 종류: Copy, Shallow Copy, Deep Copy
mutable: list, set, dict 
immutable: int, str, float, bool, unicode
'''

# copy
a_list = [1,2,3,[4,5,6],[7,8,9]]
b_list = a_list
print(id(a_list), id(b_list))    # 같은 아이디: a_list, b_list는 같은 객체를 바라본다.

b_list[2] = 100
print(a_list)
print(b_list)   
# Call by Reference: b_list에 a_list의 주소값을 전달했기 때문에, b_list를 변경해도 a_list에 똑같이 반영된다.

b_list[3][2] = 100
print(a_list)
print(b_list)

# Shallow Copy
import copy
c_list = [1,2,3,[4,5,6],[7,8,9]]
d_list = copy.copy(c_list)
print(id(c_list), id(d_list))    # 얕은 복사는 다른 아이디!

d_list[1] = 100
print(c_list)
print(d_list)

d_list[3].append(1000)
d_list[4][1] = 10000
print(c_list)
print(d_list)    # 얕은 복사는 해당 가변형 객체 안에 있는 참조형에 대해 주소값까지 전부 다른 값으로 복사해주지 않는다!

# Deep Copy
e_list = [1,2,3,[4,5,6],[7,8,9]]
f_list = copy.deepcopy(e_list)
print(id(e_list), id(f_list))

f_list[3].append(1000)
f_list[4][1] = 10000
print(e_list)
print(f_list) 
