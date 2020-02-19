# coding : utf-8

# GPIO
import RPi.GPIO as GPIO

import time

# GPIO 핀번호 할당
# 메서드에 대문자 없음! 주의!
GPIO.setmode(GPIO.BOARD)

# 핀번호(CHANNEL)
LED_R = 11 # 빨간색 LED

# 핀 속성 설정
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)

# PWM(Pulse Width Modulation) : 펄스 폭 변조
# 하이 레벨과 로우 레벨의 중간 값을 유사하게 표현하는 신호 방식
# PWM 객체 생성 : 11번 핀, 주파수 - 100Hz
p = GPIO.PWM(LED_R, 100)



import tkinter as tk

# 윈도우 객체 생성
window = tk.Tk()
window.geometry('400x400')

# 변수 설정 : 이전 dc 리스트. 사용자 입력
led_value = tk.DoubleVar()
led_value.set(0)

# duty 값 변경하는 함수
def change_duty():
    p.ChangeDutyCycle(led_value.get())

# 슬라이드 객체
# 레이블(LED 밝기 조정), 수 범위(0~100)
slide = tk.Scale(
    window,
    label='LED 밝기 조정',
    orient='h', # 수평 방향
    from_=0, # 언더바 주의
    to=100,
    variable=led_value,
    command=change_duty
    )


slide.pack()

window.mainloop()

#############################################

# PWM 정지
p.stop()

# GPIO 개방
GPIO.cleanup()