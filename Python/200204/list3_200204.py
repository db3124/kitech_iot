# list 생성 : []
list_a = [1, 2, 3]
list_b = [1, 2, 1, 2]

# remove를 이용한 요소 삭제 : 요소 값으로 삭제
print('-------list_b 요소 삭제 remove-------')
list_b.remove(1)
print(list_b)

# clear()를 이용한 요소 삭제 : 요소 값으로 삭제
print('-------list_b 요소 삭제 clear()-------')
list_b.clear()
print(list_b) 

# list에 요소 추가 append : 리스트 뒤에 요소 추가
print('-------list 요소 추가 append-------')
list_a.append(4)
print(list_a)
list_a.append(5)
print(list_a)

# list에 요소 추가 insert : 특정 index에 요소 추가
print('-------list 요소 추가 insert-------')
list_a.insert(0, 0)
print(list_a)
list_a.insert(1, [100])
print(list_a)

# list에 다른 list 추가 extend
print('-------다른 list 추가 extend-------')
list_a.extend([7, 77, 777])
print(list_a)

# list 연결 연산자 사용 시 원본에 변화 없음
#print(list_a + [42, 22])
#print(list_a)

# list 요소 삭제 : del 키워드, pop
print('-------list 요소 [0] 삭제 del-------')
del list_a[0]
print(list_a)

print('-------list 요소 (0) 삭제 pop-------')
list_a.pop(0)
print(list_a)

# list 요소 삭제 : del 키워드 범위 삭제
print('-------list 요소 [2:4] 삭제 del-------')
del list_a[2:4]
print(list_a)
print('-------list 요소 [2:] 삭제 del-------')
del list_a[2:]
print(list_a)

# in 연산자로 요소 존재 유무 확인 : True or False
print('-------in으로 요소 존재 유무 확인-------')
chkk_1 = 1000 in list_a
print('list_a 요소 중에 1000이 있는가? ', chkk_1)
chk_2 = 1 in list_a
print('list_a 요소 중에 1이 있는가? ', chk_2)