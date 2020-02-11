# 데이터 저장을 위한 class
# 기능 class -> 기능 모듈
# 데이터를 저장하고 있는 배열 또는 리스트 -> []
# 기능 메서드 : 입력(리스트에), 삭제(리스트에서), 검색, 전체 출력

#from phonebook_class import PhoneInfo

# class 정의 : PhoneInfo
# 속성 : name, phonenumber, birthday
# 기능 : showInfo

import sqlite3

# DB에 연결
con = sqlite3.connect('phonebook')

# 커서 생성
cur = con.cursor()

def insertMember():
    print('====================================')
    name = input('이름을 입력해주세요. >>')
    pNum = input('전화번호를 입력해주세요.(01X-YYYY-ZZZZ) >>')
    bDay = input('생년월일을 입력해주세요.(YYYYMMDD) >>')

    # SQL 실행
    sql_insert = "insert into phonebook_table values('{}', '{}', {})".format(
        name, pNum, bDay
    )

    cur.execute(sql_insert)

    con.commit()

# 리스트 출력하는 메서드
def showList():
    sql_select = 'select * from phonebook_table'

    cur.execute(sql_select)

    print('====================================')
    print('이름\t전화번호\t생년월일')

    while True:
        row = cur.fetchone() # 반환할 행이 없으면 None 반환
    
        if row == None:
            break

        print('{}\t{}\t{}'.format(
            row[0], row[1], row[2]
    ))

# 정보 검색하는 메서드
def searchInfo():
    print('=============검색(이름)==============')

    keyword = input('찾고자 하는 이름을 입력해주세요. >>')

    # SQL 실행
    sql_insert = "select * from phonebook_table where name='{}'".format(keyword)

    cur.execute(sql_insert)

    print('====================================')
    print('이름\t전화번호\t생년월일')
    
  
    while True:
        row = cur.fetchone() # 반환할 행이 없으면 None 반환
        
        if row == None:
            #print('(찾고자 하는 이름이 없습니다.)')
            break

        print('{}\t{}\t{}'.format(row[0], row[1], row[2]))


        
# 정보 삭제하는 메서드
def deleteInfo():
    print('==============삭제(이름)===============')

    keyword = input('삭제하고자 하는 이름을 입력해주세요. >>',)
    
    # SQL 실행
    sql_insert = "delete from phonebook_table where name = '{}'".format(keyword)

    cur.execute(sql_insert)
    
    # print('정상적으로 삭제되었습니다.')
        

# con.close()





        