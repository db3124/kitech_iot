# if2 개선
# 모듈 호출
# 날짜 시간 관련 모듈 호출
import datetime  as t

# 현재 시간 구하기
now = t.datetime.now()

print(now)
print(now.year, '년')
print(now.month, '월')
print(now.day, '일')
print(now.hour, '시')
print(now.minute, '분')
print(now.second, '초')

# 봄
if 3 <= now.month <= 5:
    print('이번 달은 {}월로, 봄입니다.'.format(now.month))
elif 6 <= now.month <= 8: # 여름
    print('이번 달은 {}월로, 여름입니다.'.format(now.month))
elif 9 <= now.month <= 11: # 가을
    print('이번 달은 {}월로, 가을입니다.'.format(now.month))
else: # 겨울
    print('이번 달은 {}월로, 겨울입니다.'.format(now.month))
