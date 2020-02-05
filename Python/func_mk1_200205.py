# 사용자 함수의 정의

def print_3_times():
    print('안녕')
    print('안녕')
    print('안녕')

print_3_times()
# print_3_times(a)

def print_n_items(value, n):
    for i in range(n):
        print(value)

print_n_items("hello", 3)