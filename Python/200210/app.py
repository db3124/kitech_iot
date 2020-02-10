from flask import Flask

# 서버 생성
app = Flask(__name__)

# 함수 정의
@app.route('/')
def hello():
    return '<h1>Hello Python :)</h1>'
s
@app.route('/hello')
def hello1():
    return '<h1>Hello hello</h1>'