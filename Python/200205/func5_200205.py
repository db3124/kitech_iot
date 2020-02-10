# 리스트 내포
# 비어 있는 리스트 선언
list_a = []

# 반복문을 통해 list_a에 요소(데이터) 추가
for i in range(0, 20, 2): # 0, 2, 4, 6, ... ,16, 18
    list_a.append(i*i) # 0의 제곱, 2의 제곱...

# list 출력
print('----list_a 출력----')
print(list_a)

# 리스트 이름 = [표현식(결과값) for 반복자 in 반복할 수 있는 것 if 조건문]
print('----리스트 내포----')
list_b = [i*i for i in range(0, 20, 2)]
print(list_b)

print('----조건 활용 리스트 내포----')
list_c = [i*i for i in range(0, 20, 2) if i>10]
print(list_c)

array = ['사과', '복숭아', '수박', '레몬', '키위']
output = [f for f in array if f != '수박']
print(array)
print(output)
