# 딕셔너리 선언 {value, ...}
# key -> int, str, bool
# value -> 숫자, 문자열, bool, list, dic

# 딕셔너리 {키:값, 키:값, 키:값...}
dic_1 = {
    'name' : '홍길동',
    'phoneNumber' : '01077778888',
    'birthday' : 19900505
}

print('-----dic_1-----')
print(dic_1)

print('-----dic_1 키:값 추가-----')
dic_1['age'] = 20
print(dic_1)

# 데이터 삭제 : del
print('-----key가 birthday인 요소 삭제-----')
del dic_1['birthday']
print(dic_1)

# print('이름 : ', dic_1['name'])
# print('전화번호 : ', dic_1['phoneNumber'])
# print('생일 : ', dic_1['birthday'])

# 기존의 데이터 변경 : key변경 x, value 값을 변경
print('-----이름 데이터 변경-----')
dic_1['name'] = '김연아'
print(dic_1)

# 사용자에게서 key 값을 입력받는다.
key_name = input('찾고자 하는 Key 입력 :')

get_value = dic_1.get(key_name) # 키가 존재하지 않는다->None

# if key_name in dic_a:
if get_value:
    print(get_value)
else:
    print('찾으시려는 Key가 존재하지 않습니다.')

for key in dic_1:
    print(key, ':', dic_1[key])

name = '이름'
type = '유형'
dic_2 = {
    name : '7D 망고절임',
    type : '망고절임'
}

print(dic_2)
