# DML
import sqlite3

# DB에 연결
con = sqlite3.connect('phonebook')

# 커서 생성
cur = con.cursor()

sql_select = 'select * from phonebook_table'

cur.execute(sql_select)

print('이름\t전화번호\t생년월일')

while True:
    row = cur.fetchone() # 반환할 행이 없으면 None 반환
    
    if row == None:
        break

    print('{}\t{}\t{}'.format(
        row[0], row[1], row[2]
    ))

con.close()
