# 데이터 wj장을 위한 class
# 기능 class -> 기능 모듈
# 데이터를 저장하고 있는 배열 또는 리스트 -> []
# 기능 메서드 : 입력(리스트에), 삭제(리스트에서), 검색, 전체 출력

# 친구의 정보를 저장하는 리스트
pBook = []

def insertMember():
    name = input('이름을 입력해주세요. >>')
    pNum = input('전화번호를 입력해주세요. >>')
    bDay = input('생일을 입력해주세요. >>')

    member = {
        'name' : name,
        'phonenumber' : pNum,
        'birthday' : bDay
    } 

    pBook.append(member)

def showList():
    for member in pBook:
        print(member)
