# coding: utf-8 
# 한글 주석이 되도록 함.

# GPIO 라이브러리 호출 
import RPi.GPIO as GPIO

import tkinter as tk

import time

# 핀 번호 할당으로 처리: 핀 번호 설정
GPIO.setmode(GPIO.BOARD)

# 핀 번호 설정: Channel 번호
LED_R = 11
LED_G = 16
LED_Y = 22

# 11번 채널(핀 번호)을 출력 핀을 등록, 초기 출력은 로우레벨(low level), Low = 0, False
GPIO.setup(LED_R, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_Y, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_G, GPIO.OUT, initial = GPIO.LOW)


print ('=====================>LED_R: ', GPIO.input(LED_R))
print ('=====================>LED_G: ', GPIO.input(LED_G))
print ('=====================>LED_Y: ', GPIO.input(LED_Y))


# 하이 레벨 출력 = 점등
def func_g():
    if GPIO.input(LED_G): # 1 : ON
        btn_g.configure(text='초록등 - OFF')
    else: # 0 : OFF
        func_clear()
        btn_g.configure(text='초록등 - ON')

    GPIO.output(LED_G, not GPIO.input(LED_G))

def func_y():
    if GPIO.input(LED_Y): # 1 : ON
        btn_y.configure(text='노란등 - OFF')
    else: # 0 : OFF
        func_clear()
        btn_y.configure(text='노란등 - ON')

    GPIO.output(LED_Y, not GPIO.input(LED_Y))

def func_r():
    if GPIO.input(LED_R): # 1 : ON
        btn_r.configure(text='빨간등 - OFF')
    else: # 0 : OFF
        func_clear()
        btn_r.configure(text='빨간등 - ON')

    GPIO.output(LED_R, not GPIO.input(LED_R))

# channel 값을 0
def func_clear():
    GPIO.output(LED_G, False)
    GPIO.output(LED_Y, 0)
    GPIO.output(LED_R, GPIO.LOW)

# 윈도우 객체
window = tk.Tk()

window.geometry('400x400')

# label 객체 생성
label = tk.Label(window, text="버튼을 눌러서 LED 점등을 하세요.")

# button
btn_g = tk.Button(window, text='초록등 - ON', command=func_g)
btn_y = tk.Button(window, text='노란등 - ON', command=func_y)
btn_r = tk.Button(window, text='빨간등 - ON', command=func_r)

# 위젯 배치 
label.pack()
btn_g.pack()
btn_y.pack()
btn_r.pack()

# 윈도우 출력
window.mainloop()

# GPIO 개방
GPIO.cleanup()



