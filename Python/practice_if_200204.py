# 사용자에게 정수 데이터를 입력 받는다.
# 데이터를 비교해서 양수/음수/0으로 구분해서 출력받음

# 데이터 입력 받기
number = input('정수 입력>>>')
number = int(number)

# 양수
if number > 0:
    print('양수')

# 0
if number == 0:
    print(0)

# 음수
if number < 0:
    print('음수')