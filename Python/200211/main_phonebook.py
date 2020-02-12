from module_basic.phonebook import phonebookmanager as pbm
import sys

while True:
    print('메뉴 : \n(1) 데이터 입력 \n(2) 전체 출력 \n(3)검색 \n(4)삭제 \n(5) 종료')
    choice = input('메뉴 번호를 입력해주세요. >>')

    if choice == '1':
        pbm.insertMember()
    elif choice == '2':
        pbm.showList()
    elif choice == '3':
        pbm.searchInfo()
    elif choice == '4':
        pbm.deleteInfo()
    elif choice == '5':
        # break
        sys.exit
    else :
        print('메뉴 번호를 확인해주세요.')
        print('====================================')
