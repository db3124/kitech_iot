# DML
import sqlite3

# DB에 연결
con = sqlite3.connect('sample')
cur = con.cursor()

# SQL 실행
sql_insert = "insert into userTable values ('shine', 'twinkle', 'mno@test.com', 2000)"

cur.execute(sql_insert)


con.commit()
con.close()