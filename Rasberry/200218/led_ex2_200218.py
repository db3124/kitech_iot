# coding : utf-8

# GPIO 라이브러리 호출
import RPi.GPIO as GPIO

import tkinter as tk

# time 모듈
import time

# 핀번호로 제어 : 핀 번호 할당 -> 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BOARD)

# 사용할 핀번호 : channel 번호
LED_W = 11

# 11번 채널(핀번호)을 출력 핀으로 등록, 초기 출력은 로우레벨
GPIO.setup(LED_W, GPIO.OUT, initial=GPIO.LOW)

print('=======> LED_W :', GPIO.input(LED_W))

def func():
    GPIO.output(LED_W, not GPIO.input(LED_W))
    # time.sleep(3)

# 윈도우 객체
window = tk.Tk()

window.geometry('400x400')

# label 객체 생성
label = tk.Label(window, text='버튼을 눌러 LED 점등을 하세요.')

# button 객체 생성
btn = tk.Button(window, text='LED_W', command=func)

# 위젯 배치
label.pack()
btn.pack()

# 윈도우 출력
window.mainloop()

# GPIO 개방
GPIO.cleanup()