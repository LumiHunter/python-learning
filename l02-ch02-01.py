# 객체 지향 프로그래밍 -> 코드의 재사용, 코드 중복 방지, 쉬운 유지보수... 대형프로젝트
# 규모가 큰 프로젝트 -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

# 차량1
from typing import Any


car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_1 = 'Bmw'
car_detail_1 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_1 = 'Audi'
car_detail_1 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# 리스트 구조: 관리가 불편, 인덱스 접근 시 실수 가능성, 삭제 불편. (하나가 지워지면 전체 인덱스가 달라지므로)
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400,'price': 8000},
    {'color': 'Black','horsepower': 270 ,'price': 5000},
    {'color': 'Silver','horsepower': 300,'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()

# 딕셔너리 구조: 코드 반복 지속, 중첩 문제(키), 키로 조회했을 때 예외 처리 등

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400,'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'Black','horsepower': 270 ,'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver','horsepower': 300,'price': 6000}},
]


del car_dicts[1]
print(car_dicts)

print()

# 클래스 구조: 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 클래스 자체를 print 할 때(1순위)
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    # 좀 더 엄격한 객체 정보를 print 할 때(2순위): 개발자용, str이 없으면 대체로 출력됨.
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
    # 인스턴스를 삭제할 때 
    def __reduce__(self):
        pass
        
car1 = Car('Ferrari',{'color': 'White', 'horsepower': 400,'price': 8000})
car2 = Car('Bmw',{'color': 'Black','horsepower': 270 ,'price': 5000})
car3 = Car('Audi',{'color': 'Silver','horsepower': 300,'price': 6000})

print(car1)
print(car2.__dict__)    # 해당 객체의 네임스페이스에 저장된 속성 정보만 모두 보여주기. (딕셔너리)
print(dir(car3))    # 네임스페이스에 저장된 것 모든 메타 데이터 보여주기. 모든 클래스는 Object를 상속 받기 때문에 __init__, __dict__ 등의 매직 메소드들을 포함한다.(리스트)

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

for x in car_list:
    print(x)
    print(repr(x))

print(car_list)    # 리스트에서 프린트할 때는 repr 형태로.