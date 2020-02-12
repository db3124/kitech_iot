from tkinter import *

# 윈도우도 위젯이다.
window=Tk()

window.title('버튼 정렬')

window.geometry('400x400')

btn_1=Button(window, text='btn-1')
btn_2=Button(window, text='btn-2')
btn_3=Button(window, text='btn-3')

# 수평 방향 정렬 : side=LEFT/RIGHT
# btn_1.pack(side=LEFT)
# btn_2.pack(side=LEFT)
# btn_3.pack(side=LEFT)

# 수직 방향 정렬 : side=TOP/BOTTOM
# btn_1.pack(side=TOP)
# btn_2.pack(side=TOP)
# btn_3.pack(side=TOP)

#  위젯의 폭 설정 : fill=X/Y
btn_1.pack(fill=X, padx=10, pady=10, ipadx=30, ipady=30)
btn_2.pack(fill=X, padx=10, pady=10, ipadx=30, ipady=30)
btn_3.pack(fill=X, padx=10, pady=10, ipadx=30, ipady=30)

window.mainloop()