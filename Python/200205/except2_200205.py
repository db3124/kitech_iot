list_ex = ['52', '35', 'hello', '2', '56']

list_result = []

for item in list_ex:
    try: # 예외 가능성이 있는 코드
        float(item)
        # list_result.append(item)
    except Exception as e: # 예외가 발생했을 때
        # pass
        print('type(e) :', type(e))
        print('Exception e :', e)
    else: # 예외 발생하지 않았을 때
        list_result.append(item)
    finally: # 무조건 실행할 코드
        print('프로그램을 종료합니다.')

print(list_ex)
print(list_result)