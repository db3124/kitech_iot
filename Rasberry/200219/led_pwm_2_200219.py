# coding : utf-8

# GPIO
import RPi.GPIO as GPIO

import time

# GPIO 핀번호 할당
# 메서드에 대문자 없음! 주의!
GPIO.setmode(GPIO.BOARD)

# 핀번호(CHANNEL)
LED_R = 11 # 빨간색 LED

# 듀티비(밝기 목록) : 0.0~100.0(순차적)
dc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 50, 70, 100]

# 핀 속성 설정
GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)

# PWM(Pulse Width Modulation) : 펄스 폭 변조
# 하이 레벨과 로우 레벨의 중간 값을 유사하게 표현하는 신호 방식
# PWM 객체 생성 : 11번 핀, 주파수 - 100Hz
p = GPIO.PWM(LED_R, 100)

# PWM  신호 출력 
p.start(0) # 듀티비

# 무한 반복
while 1:
    # 듀티 비를 0부터 100까지 목록에 따라 변경
    for val in dc:
        p.ChangeDutyCycle(val)
        # 0.1초 대기
        time.sleep(0.1)
    # 목록 나열 순서를 역순으로 변경
    dc.reverse()
        # 0.1초 대기
    time.sleep(0.1)

# PWM 정지
p.stop()

# GPIO 개방
GPIO.cleanup()