import RPi.GPIO as GPIO

import time

led=16
pir_s=25

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)

GPIO.setup(pir_s, GPIO.IN)

try:
    while True:
        if GPIO.input(pir_s) == True:
            print("Sensor on")
            GPIO.output(led, True)
            time.sleep(5)
        else:
            print("Sensor off")
            GPIO.output(led, False)
        
except KeyboardInterrupt:
    GPIO.cleanup()