# DML
import sqlite3

# DB에 연결
con = sqlite3.connect('phonebook')

# 커서 생성
cur = con.cursor()

# SQL 실행
sql_insert = "select * from phonebook_table where name='yuna'"

cur.execute(sql_insert)

con.commit()
con.close()