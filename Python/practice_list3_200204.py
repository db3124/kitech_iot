# list 생성 : []
list_a = [1, 2, 3]

# list에 요소 추가 append : 리스트 뒤에 요소 추가
list_a.append(4)
print(list_a)
list_a.append(5)
print(list_a)

# list에 요소 추가 insert : 특정 index에 요소 추가
list_a.insert(0, 0)
print(list_a)
list_a.insert(1, [100])
print(list_a)

# list에 다른 list 요소를 추가 extend
list_a.extend([7, 77, 777])
print(list_a)
print(list_a + [42, 22]) # 리스트 연결 연산자 사용 시 원본에 변화 없음
print(list_a)