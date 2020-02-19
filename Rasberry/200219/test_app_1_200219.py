# coding:utf-8

# flask
from flask import Flask
# request param
from flask import request
# CORS
from flask_cors import CORS
# GPIO 
import RPi.GPIO as GPIO

#########################################################

# GPIO 핀번호 할당
# 메서드에 대문자 없음! 주의!
GPIO.setmode(GPIO.BOARD)

# 핀번호(CHANNEL)
LED_R = 11 # 빨간색 LED

# 핀 속성 설정
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)

# PWM 객체 생성 : 11번 핀, 주파수 - 100Hz
p = GPIO.PWM(LED_R, 100)

# PWM 신호 출력
p.start(0)

# duty 값 변경하는 함수
def change_duty(dc):
    p.ChangeDutyCycle(dc)

#########################################################
app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    # 파라미터 객체에 담아서 전달
    led = request.args.get('led', 'g') # 디폴트값 g
    p_val = request.args.get('p_val', '0') # 디폴트값 0

    change_duty(int(p_val))

    return led + ' : ' + p_val

if __name__ == '__main__':
    app.run(host='192.168.0.66', port='5000', debug=False)