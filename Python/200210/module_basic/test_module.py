# 변수
PI = 3.141592

# 함수 : 사용자의 데이터 입력값을 반환하는 기능
def number_input():
    result = input('숫자 입력>')
    return float(result)

# 함수 : 원의 둘레를 구하고 값을 반환하는 기능
def get_circumference(radius):
    return 2*PI*radius

# 함수 : 원의 면적을 구하고 값을 반환하는 기능
def get_circle_area(radius):
    return PI*radius*radius

# 테스트 코드
if __name__ == '__main__':
    print(__name__)
    print(get_circumference(10))
    print(get_circle_area(10))