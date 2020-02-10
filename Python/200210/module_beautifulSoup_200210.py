# from 패키지명 import 모듈
from bs4 import BeautifulSoup as bs
from urllib import request

# urlopen() 함수를 이용해서 기상청 데이터 가져오기
target = request.urlopen('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1165051000')
soup = bs(target, 'html.parser')

# data = target.read()
# print(data)

print(soup.find('title').string)

for fdata in soup.find_all('data'):
    print(fdata.hour.string, '시 예보, ', end='')
    print(fdata.day.string, '0:오늘, 1:내일, 2:모래', end='')
    print('현재온도 :', fdata.temp.string, end='')
    print('강수상태 :', fdata.pty.string, end='')


#for data in soup.select('data'):
#    print(data.select)