from tkinter import *
from tkinter import messagebox

# window 생성
window = Tk()
window.title('동물 선택')
window.geometry('500x500')

# handler function
def viewFunc():
    if check_val.get()==1:
        messagebox.showinfo('', '강아지가 선택되었습니다.')
    elif check_val.get()==2:
        messagebox.showinfo('', '고양이가 선택되었습니다.')
    elif check_val.get()==3:
        messagebox.showinfo('', '거북이가 선택되었습니다.')
    else:
        messagebox.showinfo('', '잘못된 선택입니다.')

# 화면 구성
label_title=Label(window, text='좋아하는 동물 투표',font=('굴림체', 30))

# radio 선택 값 저장할 변수
check_val=IntVar()
label_radio_1=Radiobutton(window, text='강아지', variable=check_val, value=1, command=viewFunc)
label_radio_2=Radiobutton(window, text='고양이', variable=check_val, value=2, command=viewFunc)
label_radio_3=Radiobutton(window, text='거북이', variable=check_val, value=3, command=viewFunc)


btn = Button(window, text='확인', command=quit)

# 위젯 배치 : 실제 화면 출력
label_title.pack()
label_radio_1.pack()
label_radio_2.pack()
label_radio_3.pack()
btn.pack()

# window 출력(위젯을 감싸고 있는 기본 틀)
window.mainloop()