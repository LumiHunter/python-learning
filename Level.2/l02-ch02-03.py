class Car():
    """
    Car Class
    Author: Hwang
    Date: 2024.05.16
    Description: Class, Static, Instance Method
    """
    # 클래스 변수: 모든 인스턴스가 공유하고 있음.
    price_per_raise = 1.0
    
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
    
    # Instance Method: self-객체의 고유한 속성 값을 사용
    # 일반적으로 인스턴스 변수에 직접 접근하게 하지 않고, 메소드를 통해 반환해도 좋은 것만 골라서 접근할 수 있도록 한다.
    
    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info: {} {}'.format(self._company, self._details.get('price')))
    
    def get_price(self):
        return 'Before Car price -> company: {}, price: {}'.format(self._company, self._details.get('price'))
    
    def get_price_calc(self):
        return 'After Car price -> company: {}, price: {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    # Class Method: 클래스를 인자로 받는 메소드! 클래스 변수에 관련한 일을 함.
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased')
    
    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry, This car is not Bmw'
    
car1 = Car('Ferrari',{'color': 'White', 'horsepower': 400,'price': 8000})
car2 = Car('Bmw',{'color': 'Black','horsepower': 270 ,'price': 5000})

# 가격 정보-인스턴스 변수(직접 접근): not recommended
print(car1._details.get('price'))
print(car2._details['price'])

print(car1.get_price())
print(car2.get_price())

# 인상율-클래스 변수(직접 접근): not recommended
Car.price_per_raise = 1.4

Car.raise_price(1.6)

print(car1.get_price_calc())
print(car2.get_price_calc())

# Static Method는 객체로도, 클래스로도 호출해도 됨!
print(car1.is_bmw(car1))
print(Car.is_bmw(car2))