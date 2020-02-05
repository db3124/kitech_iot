# 딕셔너리 생성
dic_ex = {
    "key1" : "value-1",
    "key2" : "value-2",
}

dic_ex['key3'] = "value-3"

print(dic_ex)

for key in dic_ex:
    pass
    #print('{} = {}'.format(key, dic_ex[key]))

# items() 함수 출력
print('--items() 함수 출력--')
dic_ex_items = dic_ex.items()
print(dic_ex_items)

for k, v in dic_ex.items():
    print('dic_ex[{}] = {}'.format(k, v))