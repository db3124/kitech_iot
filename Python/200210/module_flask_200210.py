from flask import Flask

# 서버 생성
app = Flask(__name__)

# 함수 정의
@app.route('/')
def hello():
    return '<h1>Hello Python :)</h1>'