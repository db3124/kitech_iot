import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SRV = 13

GPIO.setup(SRV, GPIO.OUT)

# 주파수 설정
freq = 100.0

# 각도 최소, 최대
deg_min = 0.0
deg_max = 180.0

dc_min = 5.0
dc_max = 22.0

def convert_dc(deg):
    return ((deg-deg_min)*(dc_max-dc_min)/(deg_max-deg_min)+dc_min)

p = GPIO.PWM(SRV, freq)

try:
    while 1:
        # 듀티 비 설정
        dc = convert_dc(float(90))
        # PWM 신호 듀티 비를 견경해서 PWM 신호 출력
        p.ChangeDutyCycle(dc)
        # 1초 대기
        time.sleep(2)

except KeyboardInterrupt:
    pass







p.start(0)



p.stop()

GPIO.cleanup()

