# 문자열을 다루는 기본 함수
# string_str = 'Hello Python'

# string_list = string_str.split(" ")
# print(string_list)

# string_str = "001code1234spaceA15000"
string_str = "001|code1234|spaceA|15000"
string_list = string_str.split("|")
print("PK : ", string_list[0])
print("Code : ", string_list[1])
print("Name : ", string_list[2])
print("Price : ", int(string_list[3])*1.15)

print(string_str.upper())
print(string_str.lower())

string_a = "{}".format(19)
print(string_a)
print(type(string_a))

string_b = "{}원".format(19000)
print(string_b)
print(type(string_b))

string_c = "{}, {}, {}".format(5000, 6000, 7000)
print(string_c)
print(type(string_c))

string_d = "{}, {}, {}".format('문자열', 6000, True)
print(string_d)
print(type(string_d))

# 사용자 데이터 입력
# age = input('나이 입력 : ')
# print(type(age))
# print(age)

# string_a = input('숫자 입력>>>')
# string_b = input('다른 숫자 입력>>>')

# int_a = int(string_a)
# int_b = int(string_b)

# print(string_a+string_b)
# print(int_a+int_b)

# 숫자 연산
print('-----숫자 연산-----')
print('5+7=', 5+7)
print('7-5=', 7-5)
print('7*5=', 7*5)
print('7/5=', 7/5)
print('7//5=', 7//5)
print('7%5=', 7%5)

print('2**8=', 2**8)
print('2**9=', 2**9)
print('2**10=', 2**10)

print('First Python') # print 실행
print("""\
안녕
나는
visual
code\
야""")

print('Python '*3)
print(5*'Python')

a = '안녕하세요'
print(a[1:3])
print(len(a))

print(a[0]); print(a[-5])
print(a[1]); print(a[-4])
print(a[2]); print(a[-3])
print(a[3]); print(a[-2])
print(a[4]); print(a[-1])


## 식별자 주의 사항
# 키워드, 함수/모듈/클래스 이름과 동일하게 사용하면 안 됨
print('-----식별자(identifier)-----')
# str = 'abc' # 기존의 str 함수가 변수 str 변경 -> 오류 아님
# print(str(123))
# print(str)


# 기본 내장 함수 pow : pow(x,y) : x의 y승
print('-----pow-----')
print(pow(2,2))
print(pow(2,-1))

# 기본 내장 함수 type
print('-----type-----')
print(type(-1))
print(type('whattype'))
print(type([1,2,3,4,5]))

# 기본 내장 함수 range
print('-----range-----')
a = range(0,10,2)
print(a)

# 기본 내장 함수 str
print('-----str-----')
print(str(1))
print(str([1,2,3,4]))
print(str([1,'word',3,4]))
print(str('String'))

# 기본 내장 함수 chr : 정수 형태의 아스키 코드 값을 입력 받아, 해당 문자 반환
print('-----chr-----')
print(chr(90))
print(chr(100))

# 기본 내장 함수 max
print('-----max-----')
print(abs(5))
print(abs(-5))

a = 10
b = 50
nums = [1,2,3,4,5,6,7,8,9,10] # list
names = 'python'

print(max(a, b))
print(max(nums))
print(max(names))

# 기본 내장 함수 min
print('-----min-----')
print(min(a, b))
print(min(nums))
print(min(names))
