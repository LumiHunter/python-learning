'''
keyword: Shallow Copy & Deep Copy
'''
'''
객체의 복사 종류: Copy, Shallow Copy, Deep Copy
가변: list, set, dict 
'''

# copy
a_list = [1,2,3,[4,5,6],[7,8,9]]
b_list = a_list
print(id(a_list), id(b_list))    # 같은 아이디: a_list, b_list는 같은 객체를 바라본다.

b_list[2] = 100
print(a_list)
print(b_list)   
# Call by Reference: b_list에 a_list의 주소값을 전달했기 때문에, b_list를 변경해도 a_list에 똑같이 반영된다.

