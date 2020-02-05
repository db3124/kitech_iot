# list 생성
ex_list = ["요소a", "요소b", "요소c", "요소d"]

# index와 요소값을 같이 출력 -1
print('--index와 요소값을 같이 출력 -1--')
idx = 0
for val in ex_list:
    print('{}번째 요소는 {}입니다.'.format(idx, val))
    idx += 1

# index와 요소값을 같이 출력 -2
print('--index와 요소값을 같이 출력 -2--')
for index in range(len(ex_list)):
    print('{}번째 요소는 {}입니다.'.format(index, ex_list[index]))

# index와 요소값을 같이 출력 -3 : enumerate() 이용
print('--index와 요소값을 같이 출력 -3--')
enum_list = enumerate(ex_list)
list_enum_list = list(enum_list)

print(enum_list)
print(list_enum_list)

for i, value in enumerate(ex_list):
    print('{}번째 요소는 {}입니다.'.format(i, value))

