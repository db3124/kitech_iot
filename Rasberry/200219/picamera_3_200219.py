# coding: utf-8
import picamera
import time
import datetime

# picamera 객체 생성
with picamera.PiCamera() as camera:
    # 해상도 설정
    camera.resolution = (640, 480)

    now = datetime.datetime.now()

    # 파일명
    file_name = '{}{}{}{}{}{}{}.jpg'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond 
    )

    camera.start_preview()

    time.sleep(3)

    camera.stop_preview()
    
    # 촬영 후 저장
    camera.capture('photo/' + file_name)