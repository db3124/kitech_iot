import threading
import datetime

count = 0

# call back function
def func_a():
    print('Timer expired')
    print('END TIME: ', datetime.datetime.now())

    global count # 전역 변수

    if count == 10:
        return 

    count += 1
    threading.Timer(3, func_a).start()

print('START TIME :', datetime.datetime.now())

threading.Timer(3, func_a).start()

# 10초 후에 함수 실행
