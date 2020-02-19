# coding : utf-8

# flask
from flask import Flask
from flask_cors import CORS

# GPIO 모듈
import RPi.GPIO as GPIO

# 핀번호 할당 설정
GPIO.setmode(GPIO.BOARD)

# 핀 번호 설정: Channel 번호
LED_R = 11 # 빨간색 LED
LED_G = 16 # 초록색 LED
LED_Y = 22 # 빨간색 LED

# 11번 채널(핀 번호)을 출력 핀을 등록, 초기 출력은 로우레벨(low level), Low = 0, False
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
# 16번 핀 출력 핀으로 등록    
GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW) 
# 22번 핀 출력 핀으로 등록    
GPIO.setup(LED_Y, GPIO.OUT, initial=GPIO.LOW)

print ('=====================>LED_R: ', GPIO.input(LED_R))
print ('=====================>LED_G: ', GPIO.input(LED_G))
print ('=====================>LED_Y: ', GPIO.input(LED_Y))

# 하이 레벨 출력 = 점등
def func_g():
    if not GPIO.input(LED_G):
        func_clear()
        
    GPIO.output(LED_G, not GPIO.input(LED_G))

    return str(GPIO.input(LED_G))

def func_y():
    if not GPIO.input(LED_Y):
        func_clear()
        
    GPIO.output(LED_Y, not GPIO.input(LED_Y))
    
    return str(GPIO.input(LED_Y))

def func_r():
    if not GPIO.input(LED_R):
        func_clear()
        
    GPIO.output(LED_R, not GPIO.input(LED_R))

    return str(GPIO.input(LED_R))

# channel 값을 0
def func_clear():
    GPIO.output(LED_G, False)
    GPIO.output(LED_Y, 0)
    GPIO.output(LED_R, GPIO.LOW)
    
# =====================앱 설정===========================
app = Flask(__name__)

CORS(app)

@ app.route('/sw_g') # switch green
def sw_g():
    return func_g()

@ app.route('/sw_y') # switch yellow
def sw_y():
    return func_y()

@ app.route('/sw_r') # switch red
def sw_r():
    return func_r()

print(__name__)
if __name__ == '__main__':
    app.run(host='192.168.0.66', port=5000, debug=False)