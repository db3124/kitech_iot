import time # 꼭 맨 위에 import 할 필요 없다
import math as m

# 만약 import할 때 모듈명과 폴더 안의 파일명이 같다면
# 파일을 먼저 불러들인다. 파일명을 겹치지 않게 주의!

# 이 파일도 모듈 중 하나. main 모듈임

# dir() : 기본 함수. 모듈에서 사용 가능한 변수, 함수이름 list
# print(dir())

print("sin(1) :", m.sin(1))
print("cos(1) :", m.cos(1))
print("tan(1) :", m.tan(1))

print("floor(2.4) :", m.floor(2.75)) # 내림
print("ceil(2.4) :", m.ceil(2.32)) # 올림
print("trunc(2.4) :", m.trunc(2.411)) # 소수점 이하 절사

print("log(100) :", m.log(100))

math =100
print(math)
print(m)