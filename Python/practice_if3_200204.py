# 양의 정수 입력 받기
number = input('양의 정수 입력>>>')
int_num = int(number)

if int_num>0:
    # 마지막 자리수 추출
    last_char = number[-1]    

    # 짝수
    if last_char in '02468':
        print('짝수')
    if int_num % 2 == 0:
        print('짝수')

    # 홀수
    if last_char in '13579':
        print('홀수')
    if int_num % 2 != 1:
        print('홀수')

if int_num <1:
    print('양의 정수가 아닙니다. 프로그램을 종료합니다.')

