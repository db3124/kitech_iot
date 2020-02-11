# 데이터 저장을 위한 class
# 기능 class -> 기능 모듈
# 데이터를 저장하고 있는 배열 또는 리스트 -> []
# 기능 메서드 : 입력(리스트에), 삭제(리스트에서), 검색, 전체 출력

#from phonebook_class import PhoneInfo

# class 정의 : PhoneInfo
# 속성 : name, phonenumber, birthday
# 기능 : showInfo

class PhoneInfo:
    # 생성자
    def __init__(self, name, phonenumber, birthday):
        self.name = name
        self.phonenumber = phonenumber
        self.birthday = birthday
    
    # 정보 출력하는 메서드
    def showInfo(self):
        print('================정보 출력================')
        print('이름 :', self.name, sep='\t')
        print('전화번호 :', self.phonenumber, sep='\t')
        print('생일 :', self.birthday, sep='\t')
        print('===============정보 출력 끝===============')

    # 이름 비교 후 동일한지 여부 결과 반환하는 메서드
    def checkInfo(self, keyword):
        return self.name == keyword

    # __str__() 함수 재정의
    def __str__(self):
        return '================정보 출력================\n 이름 : {} \n 전화번호 : {} \n 생일 : {} \n ===============정보 출력 끝==============='.format(
            self.name, self.phonenumber, self.birthday
        )

# 친구의 정보를 저장하는 리스트
pBook = []

def insertMember():
    name = input('이름을 입력해주세요. >>')
    pNum = input('전화번호를 입력해주세요. >>')
    bDay = input('생일을 입력해주세요. >>')

    # member = {
    #     'name' : name,
    #     'phonenumber' : pNum,
    #     'birthday' : bDay
    # }

    # 수정자 : cjy
    # 일시 : 2020.2.11
    # 내용 : 딕셔너리 객체 사용 -> class 객체 사용으로 변경
    member = PhoneInfo(name, pNum, bDay)
    pBook.append(member)

# 리스트 출력하는 메서드
def showList():
    for member in pBook:
        # print(member)
        # member.showInfo()

# 정보 검색하는 메서드
def searchInfo():
    print('========검색(이름)========')

    keyword = input('이름을 입력해주세요.')

    chk_num = 0 # 검색 결과가 없을 때 : 0, 있을 때 1 이상

    for member in pBook:
        if member.checkInfo(keyword):
            # member.showInfo()
            # __str__()
            print(member)
            chk_num += 1
    
    if(chk_num == 0):
        print('찾으시는 이름이 없습니다.')

# 정보 삭제하는 메서드
def deleteInfo():
    print('========삭제(이름)========')

    keyword = input('이름을 입력해주세요.')
    
    # 검색 시 위치 확인
    # search_index = 0
    del_cnt = 0

    # for member in pBook:
    #     if member.checkInfo(keyword):
    #         del pBook[search_index]
    #         del_cnt += 1
        
    #     search_index += 1

    # [(0, {}), (1, {}), (2, {})]
    for i, member in enumerate(pBook):
        if member.checkInfo(keyword):
            del pBook[i]
            del_cnt += 1

    if(del_cnt==0):
        print('찾으시는 이름이 없습니다.')
    




        