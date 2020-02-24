# coding: utf-8

import RPi.GPIO as GPIO

import time

# 핀 번호 할당 방법 : 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BCM)

# 핀 번호 할당
SRV = 13

# 출력 핀으로 설정
GPIO.setup(SRV, GPIO.OUT)

# 주파수 설정
freq = 100.0

# 각도 최소, 최대
deg_min = 0.0
deg_max = 180.0

# PWM 신호 최소, 최대
dc_min = 5.0
dc_max = 22.0

def convert_dc(deg):
    return ((deg-deg_min)*(dc_max-dc_min)/(deg_max-deg_min)+dc_min)

# PWM 객체 생성
# 출력 핀 - SRV, 주파수 - freq
p = GPIO.PWM(SRV, freq)

# PWM 신호 출력
p.start(0)

# 예외 처리
try:
    # 무한 반복
    while 1:
        # 듀티 비 설정
        dc = convert_dc(float(90))
        # PWM 신호 듀티 비를 변경해서 PWM 신호 출력
        p.ChangeDutyCycle(dc)
        # 1초 대기
        time.sleep(2)

        # 듀티 비 설정
        dc = convert_dc(float(0))
        # PWM 신호 듀티 비를 변경해서 PWM 신호 출력
        P.ChangeDutyCycle(dc)
        # 1초 대기
        time.sleep(2)

except KeyboardInterrupt:
    pass

# PWM 정지
p.stop()

GPIO.cleanup()

