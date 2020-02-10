from urllib import request
# import urllib.request as req

# urlopen() : 웹 요청
# target = request.urlopen("https://google.com")
target = request.urlopen("http://localhost:8080/sensor1/datainput.jsp?data=sensor01,11.119")
output = target.read()

print(output)
