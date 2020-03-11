from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource
import sqlite3

app = Flask(__name__)
api = Api(app)

# DB 연결
con = sqlite3.connect('sample')

# 커서 생성
cur = con.cursor()

class LedApi(Resource):
    def get(self, led_no):
        sql_select = 'select * from userTable'

        cur.execute(sql_select)
        
        result_data = {}

        while True:
            row = cur.fetchone()
        
            if row == None:
                break
            
            result_data = {
                'id':row[0],
                'name':row[1],
                'email':row[2],
                'birthday':row[3]
                }
    
            return result_data

api.add_resource(LedApi, '/rest/v2/leds/<int:led_no>')

if __name__ == '__main__' :
    app.run(debug=True)
