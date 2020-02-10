import os

# os 기본 정보 출력
print('현재 운영체제 :', os.name)
print('현재 작업 폴더 :', os.getcwd())
print('현재 작업 폴더의 내부 요소 :', os.listdir())

# 폴더 만들기 및 삭제 : 폴더 아래 파일 없을 때만 삭제 가능
os.mkdir('hello')
os.rmdir('hello')

# 파일 생성 후 파일의 이름 변경
with open('original.txt', 'w') as file:
    file.write('hello')

# 이름 변경
os.rename('original.txt', 'new.txt')

# 파일 삭제
os.remove('new.txt')

# 시스템 명령어 실행
os.system('cls')
# os.system('dir/w')
os.system('dir')