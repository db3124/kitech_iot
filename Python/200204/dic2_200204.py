# 모듈 호출
# 날짜 시간 관련 모듈 호출
import datetime  as t

list_data = []

for i in range(5):
    key_name = str(t.datetime.now())

    # 센서 측정값 가져오기
    dic_temp = {
        key_name: "{}번째 측정값".format(i+1)
        }
    # 측정 데이터 저장(list, DB, file, network)
    list_data.append(dic_temp)

    for k in range(100000):
        pass

for j in list_data:
    print(j)