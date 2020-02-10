import datetime as d

# 현재 날짜, 시간 정보
now = d.datetime.now()

# 시간 출력 : formatting
output_a = now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
print(output_a)

output_b = '{}년 {}월 {}일 {}시 {}분 {}초'.format(
    now.year, now.month, now.day, now.hour, now.minute, now.second
)
print(output_b)

output_c = now.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}'.format(
    *"년월일시분초"
))
print(output_c)

# 특정 시간 구하기
print('datetime.timedelta 시간 더하기')
after_a = now + d.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
output_d = after_a.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}'.format(
    *'년월일시분초'
))
print(output_d)

# datetime.replace() : 특정 시간 요소 변경
after_b = now.replace(hour=(now.hour+3))
output_e = after_b.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}'.format(
    *'년월일시분초'
))
print(output_e)
