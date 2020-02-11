# circle 클래스 생성
# 속성(변수) : 반지름 - radius, 외부에서 속성 참조하지 못하도록 보호
# 기능(메서드) : 원의 둘레, 넓이 

import math

class Circle:
    # 생성자
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value 


    # getter
    def get_radius(self):
        return self.__radius

    # setter
    def set_radius(self, value):
        self.__radius = value
    
    # 둘레
    def  get_circumference(self):
        return 2*math.pi*self.__radius
    
    # 넓이
    def get_area(self):
        return math.pi*self.__radius*self.__radius

# 인스턴스 생성
c_1 = Circle(0)

# setter 메서드를 통한 변수 대입
c_1.set_radius(30)
c_1.radius = 50

# getter 메서드를 통해 __radius/둘레/넓이 값 반환
print('반지름 :', c_1.get_radius(), sep='\t')
print('반지름 :', c_1.radius, sep='\t')
print('둘레 :', c_1.get_circumference(), sep='\t')
print('넓이 :', c_1.get_area(), sep='\t')