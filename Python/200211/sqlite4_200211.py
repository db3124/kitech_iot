# DML
import sqlite3

# DB에 연결
con = sqlite3.connect('phonebook')

# 커서 생성
cur = con.cursor()

# SQL 실행
sql_insert = "insert into phonebook_table values('yuna', '010-8561-3535', 19900813)"

cur.execute(sql_insert)


con.commit()
con.close()