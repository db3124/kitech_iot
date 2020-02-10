# Bool 타입으로 치환되는 상황
# 0, None, 빈 문자열 "", 빈 list -> False
# 그 외 -> True

num = 0
str_blank = ''
nums = []

if num:
    print('0은 True 처리가 됩니다.')
else:
    print('0은 False 처리가 됩니다.')

if str_blank:
    print('빈 문자열은 True 처리가 됩니다.')
else:
    print('빈 문자열은 False 처리가 됩니다.')

if nums:
    print('빈 리스트는 True 처리가 됩니다.')
else:
    print('빈 리스트는 False 처리가 됩니다.')