import sys

print('-----------------------------------')
# 명령 매개변수 출력
print('argv :\n', sys.argv)

# 현재 프로그램이 구동되고 있는 시스템 정보 출력
print('-----------------------------------')
print('getwindowsversion :\n', sys.getwindowsversion())
print('-----------------------------------')
print('copyright :\n', sys.copyright)
print('-----------------------------------')
print('version :\n', sys.version)

# 프로그램 종료
sys.exit()