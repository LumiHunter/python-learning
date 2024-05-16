class Car():
    """
    Car Class
    Author: Hwang
    Date: 2024.05.16
    """

    # _company, _details는 인스턴스 변수, self를 인자로 받는 함수들은 인스턴스 메소드.
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 클래스 자체를 print 할 때(1순위)
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    # 좀 더 엄격한 객체 정보를 print 할 때(2순위): 개발자용, str이 없으면 대체로 출력됨.
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))
    
car1 = Car('Ferrari',{'color': 'White', 'horsepower': 400,'price': 8000})
car2 = Car('Bmw',{'color': 'Black','horsepower': 270 ,'price': 5000})
car3 = Car('Audi',{'color': 'Silver','horsepower': 300,'price': 6000})

print(car1.__doc__)    # 클래스에 달린 주석 불러오기(없으면 None)
print(id(car1))
car1.detail_info()
print()

print(car1.__class__, car2.__class__)    # 객체의 클래스 불러오기
print(id(car1.__class__) == id(car2.__class__))    # 서로 다른 객체이나, 클래스가 같음!