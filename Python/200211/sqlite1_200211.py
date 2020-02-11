# sqlite3
import sqlite3

# DB 연결
con = sqlite3.connect('sample')

# 커서 생성
cur = con.cursor()

sql_select = 'select * from userTable'

cur.execute(sql_select)

print('아이디\t이름\t이메일\t생년월일')

while True:
    row = cur.fetchone() # 반환할 행이 없으면 None 반환
    
    if row == None:
        break

    print('{}\t{}\t{}\t{}'.format(
        row[0], row[1], row[2], row[3]
    ))

con.close()
